import ast



class TypeChecker(ast.NodeVisitor):
    def __init__(self):

        # map variable names to their types (there could be more than one type)
        # main is the global scope in python...kinda. Maybe I should change that. Not sure yet
        self.func: str = "main"

        self.type_map: dict[str, dict[str, list[str]]] = {self.func: {}}



    def visit_Assign(self, node: ast.Assign):
        if isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id

            if name not in self.type_map[self.func]:
                self.type_map[self.func][name] = {}

            if isinstance(node.value, ast.Constant):
                self.type_map[self.func][name].append(type(node.value.value).__name__)
            else:
                raise Exception(f"Unknown type for {node.value.value}")



    def visit_FunctionDef(self, node: ast.FunctionDef):


