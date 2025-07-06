import re

class ModiLangParser:
    def __init__(self, code):
        self.code = code
        self.lines = [line.strip() for line in code.strip().splitlines() if line.strip()]

    def parse(self):
        if self.lines[0] != "Bhaiyon aur Beheno":
            raise SyntaxError("Program must start with 'Bhaiyon aur Beheno'")
        if self.lines[-1] != "Acche din aa gaye hai":
            raise SyntaxError("Program must end with 'Acche din aa gaye hai'")

        statements = []
        for line in self.lines[1:-1]:  # Strip start/end lines
            if line.startswith("Yaad rakhiye"):
                match = re.match(r"Yaad rakhiye (\w+) ka (.+)", line)
                if not match:
                    raise SyntaxError(f"Invalid declaration: {line}")
                var_name, value = match.groups()
                statements.append(('declare', var_name, value))
            elif line.startswith("Mitron! boliye"):
                expr = line.replace("Mitron! boliye", "", 1).strip()
                statements.append(('print', expr))
            else:
                raise SyntaxError(f"Unknown statement: {line}")
        return statements
