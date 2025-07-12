from dataclasses import dataclass
from typing import Any, List, Optional

@dataclass
class VarDecl:
    name: str
    type: str
    value: str

@dataclass
class PrintStmt:
    expr: str

@dataclass
class FunctionDecl:
    name: str
    args: List[tuple]  # List of (name, type)
    return_type: str
    body: List[Any]

@dataclass
class FunctionCall:
    name: str
    args: List[str]

@dataclass
class ReturnStmt:
    expr: str

@dataclass
class ApiRequest:
    method: str
    url: str
    data: Optional[str] = None

@dataclass
class IfStmt:
    condition: str
    then_body: List[Any]
    else_body: Optional[List[Any]] = None

@dataclass
class ForLoop:
    count_expr: str
    body: List[Any]


Statement = Any
