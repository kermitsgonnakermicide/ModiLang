from modilang.ast_nodes import *
from modilang.types import check_type
import math
import requests

class ModiLangInterpreter:
    def __init__(self, statements):
        self.statements = statements
        self.env = {}
        self.functions = {}
        self.builtins = {"math": math, "str": str, "dict": dict}

    def eval_expr(self, expr):
        return eval(expr, {**self.builtins}, self.env)

    def execute_function(self, f: FunctionDecl, args):
        if len(args) != len(f.args):
            raise ValueError("Argument count congressi")
        local_env = self.env.copy()
        for (name, typ), val_expr in zip(f.args, args):
            val = self.eval_expr(val_expr)
            if not check_type(val, typ):
                raise TypeError(f"Argument '{name}' umeed {typ}")
            local_env[name] = val
        for stmt in f.body:
            if isinstance(stmt, ReturnStmt):
                return eval(stmt.expr, self.builtins, local_env)
            elif isinstance(stmt, PrintStmt):
                print(eval(stmt.expr, self.builtins, local_env))

    def run(self):
        for stmt in self.statements:
            if isinstance(stmt, VarDecl):
                val = self.eval_expr(stmt.value)
                if not check_type(val, stmt.type):
                    raise TypeError(f"Variable '{stmt.name}' umeed {stmt.type}")
                self.env[stmt.name] = val
            elif isinstance(stmt, PrintStmt):
                print(self.eval_expr(stmt.expr))
            elif isinstance(stmt, FunctionDecl):
                self.functions[stmt.name] = stmt
            elif isinstance(stmt, FunctionCall):
                func = self.functions.get(stmt.name)
                if not func:
                    raise NameError(f"Function {stmt.name} saala congressi")
                result = self.execute_function(func, stmt.args)
                self.env['_'] = result
            elif isinstance(stmt, ApiRequest):
                url = self.eval_expr(stmt.url)
                data = self.eval_expr(stmt.data) if stmt.data else None
                if stmt.method == "GET":
                    response = requests.get(url)
                elif stmt.method == "POST":
                    response = requests.post(url, json=data)
                else:
                    raise ValueError(f"Congressi method {stmt.method}")
                self.env['response'] = response.text
                print("NaMo Response:", response.status_code, response.text)