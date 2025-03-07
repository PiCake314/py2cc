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
        self.line = "int main()"
        self.indent = "" # for beauty reasons

        self.vars = set()

    def advance(self, end="", semi=True):
        if not self.line and not end: return # nothing to append

        self.lines.append(f"{self.indent}{self.line}{end}" + (";" if semi else ""))
        self.line = ""

    def scope(self):
        space = " " if self.line[-1] != " " else ""
        self.advance(f"{space}{{", semi=False)
        self.indent += "\t"

    def unscope(self):
        self.indent = self.indent[:-1]
        self.advance("}", semi=False)



    def visitBody(self, body):
        self.scope()
        for expr in body:
            self.visit(expr)
            self.advance()
        self.unscope()

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

        self.visitBody(node.body)

        if node.orelse:
            self.line = "else "
            if len(node.orelse) > 1: self.scope()

        for expr in node.orelse:
            self.visit(expr)
            self.advance()


        if len(node.orelse) > 1: self.unscope()


    def visit_While(self, node):
        self.line += "while ("
        self.visit(node.test)
        self.line += ")"

        self.visitBody(node.body)


    def visit_For(self, node):
        self.line += "for ("
        self.visit(node.target)
        self.line += " : "
        self.visit(node.iter)
        self.line += ")"

        self.visitBody(node.body)





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
