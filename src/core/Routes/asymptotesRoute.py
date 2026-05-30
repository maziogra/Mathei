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
        
        return {
            "msg": str(asintoti),
            "warning": warning
        }
    else:
        return result