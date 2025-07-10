type_table = {
    'int': int,
    'float': float,
    'str': str,
    'bool': bool,
}

def check_type(value, expected_type):
    py_type = type_table.get(expected_type)
    if py_type is None:
        raise TypeError(f"Yeh type to congressi hai!: {expected_type}")
    return isinstance(value, py_type)