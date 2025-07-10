
from modilang.ast_nodes import *
from modilang.types import check_type
import math

class ModiLangInterpreter:
    def __init__(self, statements):
        self.statements = statements
        self.env = {}
        self.functions = {}
        self.builtins = {"math": math, "str": str}

    def eval_expr(self, expr):
        return eval(expr, {**self.builtins}, self.env)

    def execute_function(self, f: FunctionDecl, args):
        if len(args) != len(f.args):
            raise ValueError("Argument count congressi hai")
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
                    raise NameError(f"Function {stmt.name} congressi hai!")
                result = self.execute_function(func, stmt.args)
                self.env['_'] = result
