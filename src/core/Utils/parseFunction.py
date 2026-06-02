import sympy as sp
from sympy.parsing.latex import parse_latex
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor
)

x = sp.Symbol("x")

# quesat è esplicitazione delle costanti che deve farsi andare bene
SAFE_LOCALS = {
    "x": x,

    "pi": sp.pi,
    "e": sp.E,

    "sin": sp.sin,
    "cos": sp.cos,
    "tan": sp.tan,
    "log": sp.log,
    "exp": sp.exp,
    "sqrt": sp.sqrt,
    "abs": sp.Abs
}

# queste sono trasformazioni di default + altre, non so cosa ci sia in standard_transformations ma la documentation diceva di fare così
TRANSFORMATIONS = standard_transformations + (
    implicit_multiplication_application,  # 2x -> 2*x
    convert_xor,  # ^ -> **
)

# questo non servirebbe ma non mi fido abbastanza della robustezza del codice per toglierlo
def fix_constants(expr: sp.Expr) -> sp.Expr:
    replacements = {
        sp.Symbol("pi"): sp.pi,
        sp.Symbol("e"): sp.E,
    }
    return expr.xreplace(replacements)


# praticamente uguale al tuo di prima
def parse_function(f: str) -> sp.Expr:
    if not isinstance(f, str):
        raise ValueError("Input must be a string")

    f = f.strip()

    if "\\" in f or "{" in f:
        try:
            expr = parse_latex(f)
            expr = fix_constants(expr)
            return expr
        except Exception as e:
            raise ValueError(f"Invalid LaTeX: {e}")

    try:
        expr = parse_expr(
            f,
            local_dict=SAFE_LOCALS,
            transformations=TRANSFORMATIONS,
            evaluate=True
        )

        expr = fix_constants(expr)
        return expr

    except Exception as e:
        raise ValueError(f"Invalid SymPy expression: {e}")