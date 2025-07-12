import argparse
from modilang.parser import ModiLangParser
from modilang.interpreter import ModiLangInterpreter

def main():
    parser = argparse.ArgumentParser(description="ModiLang Chalao, India ka bhavishya badhao!")
    parser.add_argument('filename', help='Path to Acche Din')
    args = parser.parse_args()

    with open(args.filename, 'r', encoding='utf-8') as f:
        code = f.read()

    parser = ModiLangParser(code)
    stmts = parser.parse()
    interpreter = ModiLangInterpreter(stmts)
    interpreter.run()