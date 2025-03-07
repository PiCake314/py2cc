import ast



class Visitor(ast.NodeVisitor):

    def __init__(self):
        super().__init__()
        self.lines = [
            "#include <print>",
            "#include <string>",
            "#include <vector>",
            "#include <ranges>",
            "",
            "using namespace std::literals;",
            "", "",
            # ""
        ]

        self.functions = []

        self.line = "int main()"
        self.indent = "" # for beauty reasons

        self.vars = set()


    def advance(self, end="", semi=True, comment=""):
        if not self.line.strip() and not end: return # nothing to append. Prevents adding a useless semi

        strOrEmpty = lambda s, cond: s if cond else ""

        self.lines.append(f"{self.indent}{self.line}{end}" + strOrEmpty(";", semi) + strOrEmpty(f"\t// {comment}", comment))
        self.line = ""

    def scope(self):
        space = " " if self.line and self.line[-1] != " " else ""
        self.advance(f"{space}{{", semi=False)
        self.indent += "\t"

    def unscope(self):
        self.indent = self.indent[:-1]
        self.advance("}", semi=False)


    def visitBody(self, body, unbrace=False):

        if not unbrace: self.scope()

        if unbrace: self.line += " "

        for expr in body:
            self.visit(expr)
            self.advance()

        if not unbrace: self.unscope()

    def visit_Module(self, node):
        self.visitBody(node.body)
        self.lines.append("\n\n")


    def visit_Expr(self, node):
        self.visit(node.value)


    def visit_Call(self, node):
        match node.func:
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

            case _:
                raise Exception("Unknown function")


        for arg in node.args[:-1]:
            self.visit(arg)
            self.line += ", "
        if node.args: self.visit(node.args[-1])


        self.line += ")" # closing function call paren


    def visit_Name(self, node):
        # if isinstance(node.ctx, ast.Store):
        if node.id not in self.vars: # needn't to check for ctx
            self.line += f"auto {node.id}"
            self.vars.add(node.id)
        else:
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

        for elt in node.elts[:-1]:
            self.visit(elt)
            self.line += ", "
        if node.elts: self.visit(node.elts[-1])

        self.line += "}"


    def visit_Assign(self, node):
        self.visit(node.targets[0])
        self.line += " = "
        self.visit(node.value)


    def visit_AnnAssign(self, node):
        raise NotImplementedError("Types are not supported yet!")


    def visit_AugAssign(self, node):
        self.visit(node.target) # single target
        self.line += f" {Visitor.getBinOp(node.op)}= "
        self.visit(node.value)


    def visit_BinOp(self, node):
        self.visit(node.left)
        self.line += f" {Visitor.getBinOp(node.op)} "
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

        self.visitBody(node.body, unbrace=True)

        if node.orelse:
            self.line = "else"
            self.visitBody(node.orelse, unbrace=True)

    def visit_While(self, node):
        self.line += "while ("
        self.visit(node.test)
        self.line += ")"

        self.visitBody(node.body)

    def visit_For(self, node):
        # gotta make some const analysis
        # but adding const will do the trick
        # same with the ref

        self.line += f"for (const auto& {node.target.id}"
        self.vars.add(node.target.id) 
        # self.visit(node.target)
        self.line += " : "
        self.visit(node.iter)
        self.line += ")"

        self.visitBody(node.body, unbrace=False)


    def visit_Break(self, node):
        self.line += "break"

    def visit_Continue(self, node):
        self.line += "continue"

    def visit_Pass(self, node):
        # # self.advance() # advance gets called automatically if not called already
        # pass             # so either lines here are fine
        self.advance(comment="pass")


# ====================================================================================


    def visit_FunctionDef(self, node):
        pass



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

    def getBinOp(op):
        match op:
            case ast.Add():
                return "+"
            case ast.Sub():
                return "-"
            case ast.Mult():
                return "*"
            case ast.Div():
                return "/"
            case ast.FloorDiv():
                return "//"
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