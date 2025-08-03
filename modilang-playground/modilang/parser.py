import re
from typing import List
from modilang.ast_nodes import *

class ModiLangParser:
    def __init__(self, code: str):
        self.lines = [line.strip() for line in code.strip().splitlines() if line.strip()]
        self.pos = 0

    def parse(self) -> List[Statement]:
        if self.lines[0] != "Bhaiyon aur Beheno":
            raise SyntaxError("Program must start with 'Bhaiyon aur Beheno'")
        if self.lines[-1] != "Acche din aa gaye hai":
            raise SyntaxError("Program must end with 'Acche din aa gaye hai'")

        self.pos = 1
        statements = []
        while self.pos < len(self.lines) - 1:
            line = self.lines[self.pos]
            if line.startswith("Vikas hai"):
                m = re.match(r"Vikas hai (\w+): (\w+) ka (.+)", line)
                if not m:
                    raise SyntaxError(f"Congressi variable declaration: {line}")
                var, typ, val = m.groups()
                statements.append(VarDecl(var, typ, val))
            elif line.startswith("Mitron! boliye"):
                expr = line.replace("Mitron! boliye", "", 1).strip()
                statements.append(PrintStmt(expr))
            elif line.startswith("Yojana "):
                decl = self.parse_function()
                statements.append(decl)
            elif line.startswith("Yojana se labh lein"):
                m = re.match(r"Yojana se labh lein (\w+)\((.*)\)", line)
                if not m:
                    raise SyntaxError(f"Invalid Yojana se labh lein syntax: {line}")
                fname, args = m.groups()
                arg_list = [arg.strip() for arg in args.split(",") if arg.strip()]
                statements.append(FunctionCall(fname, arg_list))
            elif line.startswith("Wapas dijiye"):
                expr = line.replace("Wapas dijiye", "", 1).strip()
                statements.append(ReturnStmt(expr))
            elif line.startswith("SchemeLaunch"):
                m = re.match(r"SchemeLaunch (.+?) se (GET|POST) karo(?: (.+))?", line)
                if not m:
                    raise SyntaxError(f"Congressi SchemeLaunch syntax: {line}")
                url_expr, method, data_expr = m.groups()
                statements.append(ApiRequest(method, url_expr.strip(), data_expr.strip() if data_expr else None))
            elif line.startswith("Agar "):
                stmt = self.parse_if()
                statements.append(stmt)
            elif line.startswith("Desh ke liye N baar("):
                stmt = self.parse_loop()
                statements.append(stmt)
            else:
                raise SyntaxError(f"Congressi statement: {line}")
            self.pos += 1

        return statements

    def parse_function(self) -> FunctionDecl:
        header = self.lines[self.pos]
        m = re.match(r"Yojana (\w+)\((.*?)\) -> (\w+):", header)
        if not m:
            raise SyntaxError(f"Invalid function declaration: {header}")
        name, args_str, ret_type = m.groups()
        args = []
        for a in args_str.split(','):
            if a.strip():
                var, typ = a.strip().split(':')
                args.append((var.strip(), typ.strip()))
        self.pos += 1
        body = []
        while self.pos < len(self.lines):
            line = self.lines[self.pos]
            if line.startswith("Yojana") or line == "Acche din aa gaye hai":
                break
            if line.startswith("Wapas dijiye"):
                expr = line.replace("Wapas dijiye", "", 1).strip()
                body.append(ReturnStmt(expr))
            elif line.startswith("Mitron! boliye"):
                expr = line.replace("Mitron! boliye", "", 1).strip()
                body.append(PrintStmt(expr))
            self.pos += 1
        self.pos -= 1
        return FunctionDecl(name, args, ret_type, body)

    def parse_if(self) -> IfStmt:
        m = re.match(r"Agar (.+) toh:", self.lines[self.pos])
        if not m:
            raise SyntaxError("Invalid Agar syntax")
        condition = m.group(1).strip()
        self.pos += 1
        then_body = []
        while self.pos < len(self.lines):
            line = self.lines[self.pos]
            if line == "Nahi toh:":
                self.pos += 1
                break
            elif line.startswith("Mitron! boliye"):
                expr = line.replace("Mitron! boliye", "", 1).strip()
                then_body.append(PrintStmt(expr))
                self.pos += 1
            elif line.startswith("Wapas dijiye"):
                expr = line.replace("Wapas dijiye", "", 1).strip()
                then_body.append(ReturnStmt(expr))
                self.pos += 1
            elif line.startswith("Yojana se labh lein"):
                m = re.match(r"Yojana se labh lein (\w+)\((.*)\)", line)
                if not m:
                    raise SyntaxError(f"Invalid Yojana se labh lein syntax: {line}")
                fname, args = m.groups()
                arg_list = [arg.strip() for arg in args.split(",") if arg.strip()]
                then_body.append(FunctionCall(fname, arg_list))
                self.pos += 1
            else:
                break
        else_body = []
        while self.pos < len(self.lines):
            line = self.lines[self.pos]
            if line.startswith("Mitron! boliye"):
                expr = line.replace("Mitron! boliye", "", 1).strip()
                else_body.append(PrintStmt(expr))
                self.pos += 1
            elif line.startswith("Wapas dijiye"):
                expr = line.replace("Wapas dijiye", "", 1).strip()
                else_body.append(ReturnStmt(expr))
                self.pos += 1
            elif line.startswith("Yojana se labh lein"):
                m = re.match(r"Yojana se labh lein (\w+)\((.*)\)", line)
                if not m:
                    raise SyntaxError(f"Invalid Yojana se labh lein syntax: {line}")
                fname, args = m.groups()
                arg_list = [arg.strip() for arg in args.split(",") if arg.strip()]
                else_body.append(FunctionCall(fname, arg_list))
                self.pos += 1
            else:
                break
        self.pos -= 1
        return IfStmt(condition, then_body, else_body or None)

    def parse_loop(self) -> ForLoop:
        m = re.match(r"Desh ke liye N baar\((.+)\):", self.lines[self.pos])
        if not m:
            raise SyntaxError("Invalid Desh ke liye loop")
        count_expr = m.group(1).strip()
        self.pos += 1
        body = []
        while self.pos < len(self.lines):
            line = self.lines[self.pos]
            if line.startswith(("Mitron! boliye", "Wapas dijiye", "Yojana se labh lein")):
                body.append(self.parse()[0])
                self.pos += 1
            else:
                break
        self.pos -= 1
        return ForLoop(count_expr, body)
