import ast


class TypeChecker(ast.NodeVisitor):
    def __init__(self):

        # map variable names to their types (there could be more than one type)
        # main is the global scope in python...kinda. Maybe I should change that. Not sure yet
        self.func: str = "main"
        self.infor = False
        self.type_map: dict[str, dict[str, set[str]]] = {self.func: {}}
        self.stack: list[dict[str, dict[str, set[str]]]] = []


    def addType(self, name: str, type: str):
        if self.func not in self.type_map: self.type_map[self.func] = {}

        self.type_map[self.func][name].add(type)


    def visit_Assign(self, node: ast.Assign):
        if isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id
            if name not in self.type_map[self.func]: self.type_map[self.func][name] = set()

            types = self.visit(node.value)
            if types is None: self.addType(name, "auto") # function call result | will concreteify later
            else:
                for type in types:
                    self.addType(name, type)



    def visit_Name(self, node):
        # built-ins | user-defined functions
        builtins = ["print", "len", "range"]
        if node.id in builtins or node.id in self.type_map: return {"_func_"}

        # a for loop variable
        if self.infor: return {"_for_"}


        return self.type_map[self.func][node.id]

    def visit_Constant(self, node):
        return {type(node.value).__name__}

    def visit_BinOp(self, node):
        types1 = self.visit(node.left)
        types2 = self.visit(node.right)

        # in case one of them is a template :sob:
        if not types1: return types2
        if not types2: return types1

        assert types1 == types2 , f'Type mismatch:\n"{types1}" from: {ast.dump(node.left, indent=4)}\n"{types2}": from: {ast.dump(node.right, indent=4)}'
        return types1

    def visit_Compare(self, node): return {bool.__name__}
    def visit_BoolOp(self, node):
        # in python, bool ops can return a value
        # return {t for t in self.visit(v) for v in node.values}.add(self.visit(node.left))
        return {bool.__name__} # however, in CC, they just return bool
    def visit_UnaryOp(self, node): return {int.__name__} # can I assume this?? 
    def visit_List(self, node): return {list.__name__}
    def visit_Dict(self, node): return {dict.__name__}
    def visit_Set(self, node): return {set.__name__}
    def visit_Tuple(self, node): return {tuple.__name__}


    def visit_FunctionDef(self, node: ast.FunctionDef):
        self.stack.append({})
        self.old_func = self.func
        self.func = node.name

        if self.func not in self.type_map: self.type_map[self.func] = {}

        for arg in node.args.args:
            self.type_map[self.func][arg.arg] = set()

        # print("Visiting function:", self.func)
        self.generic_visit(node)
        # print("Unvisiting function:", self.func)

        self.func = self.old_func
        self.stack.pop()


    def visit_For(self, node):
        self.infor = True
        type = self.visit(node.target)

        name = node.target.id
        if name not in self.type_map[self.func]: self.type_map[self.func][name] = set()
        self.addType(node.target.id, next(iter(type))) # only one type

        self.infor = False


    def visit_IfExp(self, node):
        return self.visit(node.body).union(self.visit(node.orelse))

    # def visit_Call(self, node):
    #     for arg in node.args:
    #         self.visit(arg)

    #     return super().visit_Call(node)