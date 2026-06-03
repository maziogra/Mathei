from fastapi import APIRouter, HTTPException
import sympy as sp
from core.Utils.checkFunction import checkFunction
from core.Asymptotes.asymptotes import asymptotes
from sympy.parsing.latex import parse_latex
from core.Utils.parseFunction import parse_function


router = APIRouter()

@router.get("/asymptotes")
async def get_asymptotes(f: str | None = None):
    x = sp.symbols("x")
    try:
        expr = parse_function(f)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    result = checkFunction(expr, x)
    
    if result == None:
        asintoti, warning = asymptotes(expr, x)
        
        asintoti = to_json_safe(asintoti)
        
        return {
            "msg": asintoti,
            "warning": warning
        }
    else:
        return result
    
def to_json_safe(obj):
    if isinstance(obj, dict):
        return {k: to_json_safe(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple, set)):
        return [to_json_safe(x) for x in obj]
    if hasattr(obj, "float"):
        return float(obj)
    return str(obj)