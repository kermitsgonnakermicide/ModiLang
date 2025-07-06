class ModiLangInterpreter:
    def __init__(self, statements):
        self.statements = statements
        self.env = {}

    def eval_expression(self, expr):
        try:
            return eval(expr, {}, self.env)
        except Exception as e:
            raise RuntimeError(f"Error evaluating expression '{expr}': {e}")

    def execute(self):
        for stmt in self.statements:
            if stmt[0] == 'declare':
                _, var_name, expr = stmt
                self.env[var_name] = self.eval_expression(expr)
            elif stmt[0] == 'print':
                _, expr = stmt
                print(self.eval_expression(expr))
