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
                self.type_map[self.func][name] = []

            # print(ast.dump(node))

            match node.value:
                case ast.Constant(value):
                    self.type_map[self.func][name].append(type(value).__name__)
                case ast.List(_):
                    self.type_map[self.func][name].append(list.__name__) # I think that's just "list"
                case ast.Dict(_):
                    self.type_map[self.func][name].append(dict.__name__)
                case ast.Set(_):
                    self.type_map[self.func][name].append(set.__name__)
                case ast.Tuple(_):
                    self.type_map[self.func][name].append(tuple.__name__)

                case ast.Name(id): pass

                case _:
                    raise Exception(f"Unknown type for:\n{ast.dump(node.value)}")



    # def visit_FunctionDef(self, node: ast.FunctionDef):
    #     pass

