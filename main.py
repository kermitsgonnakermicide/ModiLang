import sys
from parser import ModiLangParser
from interpreter import ModiLangInterpreter

def main(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()

    parser = ModiLangParser(code)
    statements = parser.parse()

    interpreter = ModiLangInterpreter(statements)
    interpreter.execute()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <script.modi>")
        sys.exit(1)

    main(sys.argv[1])
