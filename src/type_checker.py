import ast


class TypeChecker(ast.NodeVisitor):
    def __init__(self):

        # map variable names to their types (there could be more than one type)
        # main is the global scope in python...kinda. Maybe I should change that. Not sure yet
        self.func: str = "main"

        self.type_map: dict[str, dict[str, set[str]]] = {self.func: {}}


    def addType(self, name: str, type: str): pass


    def visit_Assign(self, node: ast.Assign):
        if isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id

            if name not in self.type_map[self.func]:
                self.type_map[self.func][name] = set()

            # print(ast.dump(node))

            match node.value:
                case ast.Constant(value):
                    self.type_map[self.func][name].add(type(value).__name__)
                case ast.List(_):
                    self.type_map[self.func][name].add(list.__name__) # I think that's just "list"
                case ast.Dict(_):
                    self.type_map[self.func][name].add(dict.__name__)
                case ast.Set(_):
                    self.type_map[self.func][name].add(set.__name__)
                case ast.Tuple(_):
                    self.type_map[self.func][name].add(tuple.__name__)

                case ast.Name(id):
                    # if id not in self.type_map[self.func]:
                    #     raise Exception(f"Variable {id} not defined")

                    # assuming name is always defined before use
                    self.type_map[self.func][name].append(self.type_map[self.func][id][0])

                case _:
                    raise Exception(f"Unknown type for:\n{ast.dump(node.value)}")



    # def visit_FunctionDef(self, node: ast.FunctionDef):
    #     pass

