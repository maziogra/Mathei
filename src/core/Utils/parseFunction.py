import sympy as sp
from sympy.parsing.latex import parse_latex

def parse_function(f: str) -> sp.Expr:
    if '\\' in f or '^' in f or '{' in f:
        try:
            result = parse_latex(f)
            print("______________________________________________Result latex", result)
            return result
        except Exception as e:
            raise ValueError(f"Formato LaTeX non valido: {e}")
    else:
        try:
            result = sp.parse_expr(f, transformations='all', evaluate=True)
            print("______________________________________________Result sympy", result)
            return result
        except Exception as e:
            raise ValueError(f"Formato sympy non valido: {e}")