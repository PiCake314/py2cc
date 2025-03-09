import sys
import os
import ast
import visitor


OUT = "outputs/"


GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

def output(file: str, stdout: bool, v: visitor.Visitor):
    if sys.argv[-1] == "debug" and not stdout: return


    sys.stdout.close = lambda: None

    ccfile = f"{OUT}{file}.cc"
    with open(ccfile, "w") if not stdout else sys.stdout as fout:
        fout.write("\n".join(v.code()))


    if not stdout: print(f"{GREEN}File {ccfile} created{RESET}")


def main():
    print(sys.argv)
    if len(sys.argv) < 3: return print(f"{RED}No file provided{RESET}")

    DIR = f"{sys.argv[1]}_tests"
    file = sys.argv[2]
    stdout = len(sys.argv) > 3 and sys.argv[3] == "stdout"

    pyfile = f"{DIR}/{file}.py"
    if not os.path.exists(pyfile): return print(f"{RED}File {pyfile} not found{RESET}")

    v = visitor.Visitor(None)
    with open(pyfile, "r") as fout:
        tree = ast.parse(fout.read())

        if sys.argv[-1] == "debug" : print(ast.dump(tree, indent=2))

        v.visit(tree)


    output(file, stdout, v)





if __name__ == "__main__":
    main()