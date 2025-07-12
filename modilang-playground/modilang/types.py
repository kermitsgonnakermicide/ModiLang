type_table = {
    'int': int,
    'float': float,
    'str': str,
    'bool': bool,
    'dict': dict,
}

def check_type(value, expected_type):
    py_type = type_table.get(expected_type)
    if py_type is None:
        raise TypeError(f"Unknown type: {expected_type}")
    return isinstance(value, py_type)
