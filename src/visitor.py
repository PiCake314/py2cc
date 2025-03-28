import ast



# Maybe not needed

# class Function:
#     def __init__(self, name, args, body):
#         self.name = name
#         self.args = args
#         self.body = body

#     def __str__(self):
#         return f"{self.name}({', '.join(self.args)})"





class Visitor(ast.NodeVisitor):

    def __init__(self, types_map):
        super().__init__()

        self.lines: list[str] = [
            "#include <print>",
            "#include <iomanip>",
            "#include <string>",
            "#include <vector>",
            "#include <unordered_map>",
            "#include <unordered_set>",
            "#include <tuple>",
            "#include <utility>",
            "#include <ranges>",
            "",
            "#include <optional>",
            "#include <variant>",
            "#include <any>",
            "", "",
            'using std::operator""s;',
            "", "", "",
            "// functions:",
            "", "", "",
            "int main()"
        ]

        self.type_map = types_map

        self.func: str = "main"
        self.functions: dict[str, list[str]] = {}
        self.in_func: bool = False

        self.line: str = ""
        self.indent: str = "" # for beauty reasons

        self.globals: set[str] = set()
        self.stack: list[set[str]] = []

        # used when function
        self.old_stack: list[set[str]] = None

        # self.vars: set[str] = set()
        self.new_env = self

        self.comment = ""

    def code(self): # should only be called once. Maybe I should add a flag, but I'll leave it for now!
        index = self.lines.index("// functions:") + 1

        for function in self.functions.values():
            self.lines[index : index] = function
            index += len(function) + 1

        self.lines.remove("// functions:")

        index = self.lines.index("int main()") + 2 # skip "main" declaration and "{"
        self.lines.insert(index, "\tstd::setprecision(2);")

        return self.lines


    def ccType(self, t: str): # returns the proper type name
        ctad = "ctad takes care of type parameter deduction"

        match t:
            case "str":
                return "std::string"
            case "list":
                self.addComment(ctad)
                return "std::vector"
            case "dict":
                self.addComment(ctad)
                return "std::unordered_map"
            case "set":
                self.addComment(ctad)
                return "std::unordered_set"
            case "tuple":
                self.addComment(ctad)
                return "std::tuple"
            case "float":
                return "double" # python floats are doubles

            # case "int":
                # technically, these are big ints.
                # Should I use long long? or use a library?? idk...
                # return "int"

            case _:
                return t # assuming there are no wrong types


    def getType(self, name):
        if name not in self.type_map[self.func]:
            raise Exception(f'Variable "{name}" not defined in "{self.func}"')

        return self.type_map[self.func][name]


    def addComment(self, comment):
        if self.comment: self.comment += f" | {comment}"
        else: self.comment = comment


    def varExists(self, name):
        return any(name in stack for stack in self.stack) or name in self.globals

    def addVar(self, name, type=""):
        self.stack[-1].add(name)
        if not type: return

        if name not in self.type_map[self.func]: self.type_map[self.func][name] = {type}
        else: self.type_map[self.func][name].add(type)

    def addEnv(self):
        self.stack.append(set())

    def endEnv(self):
        self.stack.pop()

    def advance(self, end="", *, semi=True, newline=False):
        if not self.line.strip() and not end: return # nothing to append. Prevents adding a useless semi

        strOrEmpty = lambda s, cond: s if cond else ""

        new_line = f"\n{self.indent}" if newline else ""
        semi_colon = strOrEmpty(";", semi)
        the_comment = strOrEmpty(f"\t\t\t// {self.comment}", self.comment)

        line = f"{self.indent}{self.line}{end}{new_line}" + semi_colon + the_comment

        if self.in_func:
            func_name = list(self.functions.keys())[-1]
            self.functions[func_name].append(line)
        else:
            self.lines.append(line)


        self.line = ""
        self.comment = ""

    def scope(self):
        space = " " if self.line and self.line[-1] != " " else ""
        self.advance(f"{space}{{", semi=False)
        self.indent += "\t"

    def unscope(self):
        self.indent = self.indent[:-1]
        self.advance("}", semi=False)


    def visitBody(self, body, *, unbrace=False, orelse=False):

        should_scope = not unbrace or len(body) > 1 #or orelse

        if should_scope: self.scope()
        else: self.line += " "

        for expr in body:
            self.visit(expr)
            self.advance()

        if should_scope: self.unscope()


    def visitElements(self, elts):
        for elt in elts[:-1]:
            self.visit(elt)
            self.line += ", "
        if elts: self.visit(elts[-1])


    def visit_Module(self, node):
        with self.new_env:
            self.visitBody(node.body)

        self.lines.append("\n\n")


    def visit_Expr(self, node):
        self.visit(node.value)


    def visit_Call(self, node):
        match node.func:
            # special cases first

            case ast.Name(id="print"):
                self.line += "std::println("

                self.line += '"'
                for _ in node.args: self.line += "{} "
                self.line = self.line[:-1] + '", ' # removing last space and closing quote

            case ast.Name(id="range"):
                self.line += "std::ranges::views::iota("

                if len(node.args) == 1:
                    # not sure which is better...

                    # self.line += "0, "
                    node.args.insert(0, ast.Constant(value=0)) # beginning of the range

            case ast.Name(id="len"):
                self.line += "std::ranges::size("

            case _: # should I specify ast.Name or do I allow any expression?
                self.visit(node.func)
                self.line += "("


        for arg in node.args[:-1]:
            self.visit(arg)
            self.line += ", "
        if node.args: self.visit(node.args[-1])


        self.line += ")" # closing function call paren


    def visit_Name(self, node):

        # i think it's safe to assume that any variable will have a type.
        types = set()

        # function
        if node.id in self.type_map: types = {"_func_"}

        # or a variable
        if node.id in self.type_map[self.func]: types = self.type_map[self.func][node.id]

        if not types: raise Exception(f'Variable "{node.id}" does not have a type.\nType Table: {self.type_map}')

        if not self.varExists(node.id):
            # self.line += f"auto {node.id}"
            # types = self.type_map[self.func][node.id]

            vtype: str = self.ccType(next(iter(types))) if len(types) == 1 else f"std::variant<{", ".join(map(self.ccType, sorted(types)))}>"
            self.line += f"{vtype} {node.id}"

            # self.vars.add(node.id)
            self.addVar(node.id)



        # # reading from variant
        # # only call std::visit if I'm reading from the variant
        # # and only call std::visit if I'm a variant.
        # elif isinstance(node.ctx, ast.Load) and len(types) > 1:
        #     print(node.id)
        #     print(node.types)
        #     vtype: str = f"std::variant<{", ".join(map(self.ccType, sorted(node.types)))}>"
        #     self.line += f"std::visit([](const auto& value) -> {vtype} {{ return value; }}, {node.id})"
        #     self.addComment("accessing the value")

        else: # reading
            self.line += node.id

    def visit_Constant(self, node):
        if isinstance(node.value, str):
            self.line += f'"{node.value}"s'
        elif isinstance(node.value, bool):
            self.line += str(node.value).lower()
        else:
            self.line += str(node.value)


    def visit_List(self, node):
        self.line += "std::vector{"
        self.visitElements(node.elts)
        self.line += "}"


    def visit_Dict(self, node):
        self.line += "std::unordered_map{"
        for key, value in zip(node.keys, node.values):
            self.line += "std::pair{"
            self.visit(key)
            self.line += ", "
            self.visit(value)
            self.line += "}, "
        if node.keys: self.line = self.line[:-2] # removing last comma and space
        self.line += "}"


    def visit_Set(self, node):
        self.line += "std::unordered_set{"
        self.visitElements(node.elts)
        self.line += "}"

    def visit_Tuple(self, node):
        self.line += "std::tuple{"
        self.visitElements(node.elts)
        self.line += "}"

    def visit_Subscript(self, node):
        self.visit(node.value)
        self.line += "["
        self.visit(node.slice)
        self.line += "]"



    # this had a bug this entire time ("type" instead of "types") but it didn't affect anything??
    # so I'm removing it
    # # def checkVariant(self, node, types: set[str]):
    # #     if isinstance(node.value, ast.Name): node.value.types = type


    def visit_Assign(self, node):
        target = node.targets[0] # assuming one target for now

        # variant assign
        is_varaint = isinstance(node.value, ast.Name) and len(self.type_map[self.func][target.id]) > 1
        # print(is_varaint)
        # print(self.func)
        # print(target.id)
        # print(self.type_map)
        # print(self.type_map[self.func])
        # print(self.type_map[self.func][target.id])
        if is_varaint:
            # only visit if the var doesn't exist
            # otherwize, and useless line with just the id will be added
            if not self.varExists(target.id): self.visit(target)
            self.advance()

            self.addComment("assigning to a variant requires std::visit")
            self.line += f"std::visit([&{target.id}] (const auto& value) {{ {target.id} = value; }}, "
        else:
            self.visit(target)
            self.line += " = "

        # package the type in case the assignment is a variant
        # if isinstance(target, ast.Name):
        #     self.checkVariant(node, self.type_map[self.func][target.id])
        # elif isinstance(target, ast.Subscript):
        #     self.checkVariant(node, self.type_map[self.func][target.value.id])

        self.visit(node.value)

        if is_varaint: self.line += ")" # closing the call to std::visit


    def visit_AnnAssign(self, node):
        # Should we trust the type annotations...?
        raise NotImplementedError("Types are not supported yet!")


    def visit_AugAssign(self, node):
        self.visit(node.target) # single target
        self.line += f" {self.getBinOp(node.op)}= "
        self.visit(node.value)


    def visit_BinOp(self, node):
        self.visit(node.left)
        self.line += f" {self.getBinOp(node.op)} "
        self.visit(node.right)


    def visit_BoolOp(self, node):
        self.visit(node.values[0])

        for value in node.values[1:]:
            match node.op:
                case ast.And():
                    self.line += " and "
                case ast.Or():
                    self.line += " or "

            self.visit(value)


    def visit_UnaryOp(self, node):
        op = Visitor.getUOp(node.op)
        self.line += f"{op}{" " if op == 'not' else ""}"
        self.visit(node.operand)


    def visit_Compare(self, node):
        self.visit(node.left)

        self.line += f" {Visitor.getCompOp(node.ops[0])} "

        # if the comparator is a comparison, wrap it in parens to match the semantics of python in C++
        if isinstance(node.comparators[0], ast.Compare): self.line += "("
        self.visit(node.comparators[0]) # at least one comparator is guaranteed
        if isinstance(node.comparators[0], ast.Compare): self.line += ")"


        for i, (cmp, op) in enumerate(zip(node.comparators[1:], node.ops[1:])): # first element just got done
            self.line += " and "

            self.visit(node.comparators[i]) # i is lagging behind

            self.line += f" {Visitor.getCompOp(op)} "

            self.visit(cmp)


    def visit_If(self, node):
        self.line += "if ("
        self.visit(node.test)
        self.line += ")"

        self.visitBody(node.body, unbrace=True, orelse=node.orelse)

        if node.orelse:
            self.line = "else"
            self.visitBody(node.orelse, unbrace=True)

    def visit_IfExp(self, node):
        self.visit(node.test)
        self.line += " ? "
        self.visit(node.body)
        self.line += " : "
        self.visit(node.orelse)

    def visit_While(self, node):
        with self.new_env: # new environment on top
            self.line += "while ("
            self.visit(node.test)
            self.line += ")"

            self.visitBody(node.body, unbrace=True)

    def visit_For(self, node):
        # gotta make some const analysis
        # but adding const will do the trick
        # same with the ref

        with self.new_env: # new environment on top
            self.line += f"for (const auto& {node.target.id}"
            self.addVar(node.target.id)

            # self.vars.add(node.target.id) 
            # self.visit(node.target)

            self.line += " : "
            self.visit(node.iter)
            self.line += ")"

            self.visitBody(node.body, unbrace=True)


    def visit_Break(self, node):
        self.line += "break"

    def visit_Continue(self, node):
        self.line += "continue"

    def visit_Pass(self, node):
        # # self.advance() # advance gets called automatically if not called already
        # pass             # so either lines here are fine
        self.addComment('"pass"')
        self.advance(newline=True)


# ====================================================================================


    def startFunc(self, name):
        self.func = name
        self.functions[name] = []
        self.indent = ""

        # self.vars.add(name)
        self.globals.add(name)

        self.old_stack = self.stack
        self.stack = []
        self.in_func = True



    def endFunc(self):
        self.func = "main" # always back to main..i think
        self.stack = self.old_stack
        self.old_stack = None

        self.indent = "\t"

        self.in_func = False


    def visit_FunctionDef(self, node):
        self.startFunc(node.name)

        with self.new_env:
            self.line += f"auto {node.name}("
            template_line: str = ""
            T: chr = 'T'

            for arg in node.args.args:

                # determine the type:
                vtype: str = "" 
                const: bool = "const "
                # we're only reading, never assigning.
                if arg.arg in self.type_map[self.func] and self.type_map[self.func][arg.arg]:
                    # a type can only be deduced if the var been reassigned in the template
                    # hence, no const
                    const = ""

                    types = self.getType(arg.arg)
                    vtype = self.ccType(next(iter(types))) if len(types) == 1 else f"std::variant<{", ".join(map(self.ccType, sorted(types)))}>"
                else: # otherwise, make a template
                    if not template_line:
                        template_line = f"template <typename {T}"
                    else:
                        template_line += f", typename {T}"

                    vtype = T
                    T = chr(ord(T) + 1)


                # after determining the type, now we can add the parameter
                self.line += f"{const}{vtype}& {arg.arg}, "
                self.addVar(arg.arg, vtype)

            if template_line: self.line = f"{template_line}>\n{self.line}" # add the template line if needed

            if node.args.args: self.line = self.line[:-2] # removign last comma and space

            self.line += ")"

            self.visitBody(node.body)


        self.endFunc()

    def visit_Return(self, node):
        self.line += "return "
        self.visit(node.value)


# ====================================================================================


    def getCompOp(op):
        match op:
            case ast.Eq():
                return "=="
            case ast.NotEq():
                return "!="
            case ast.Lt():
                return "<"
            case ast.LtE():
                return "<="
            case ast.Gt():
                return ">"
            case ast.GtE():
                return ">="

        raise Exception("Unknown operator")

    def getBinOp(self, op):
        match op:
            case ast.Add():
                return "+"
            case ast.Sub():
                return "-"
            case ast.Mult():
                return "*"
            case ast.Div():
                self.addComment("single div in python results in a double")
                return "/ (double)"
            case ast.FloorDiv():
                return "/"
            case ast.Mod():
                return "%"
            case ast.Pow():
                raise NotImplementedError('Exponentiation "**" operator not implemented')
            case ast.LShift():
                return "<<"
            case ast.RShift():
                return ">>"
            case ast.BitOr():
                return "|"
            case ast.BitXor():
                return "^"
            case ast.BitAnd():
                return "&"
            case ast.MatMult():
                raise NotImplementedError('Matrix multiplication "@" operator not implemented')

        raise Exception("Unknown operator")

    def getUOp(op):
        match op:
            case ast.USub():
                return "-"
            case ast.UAdd():
                return "+"
            case ast.Not():
                return "not"
            case ast.Invert():
                return "~"


    def __enter__(self):
        self.addEnv()
        return self


    def __exit__(self, exc_type, exc_value, traceback):
        self.endEnv()
        return None # don't suppress exceptions
