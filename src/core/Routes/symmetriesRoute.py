from fastapi import APIRouter, HTTPException
import sympy as sp
from core.Symmetries.Symmetries import symmetries
from core.Utils.checkFunction import checkFunction
from core.Utils.parseFunction import parse_function

router = APIRouter()

@router.get("/symmetries")
async def get_symmetries(f: str | None = None):
    x = sp.symbols("x")
    try:
        expr = parse_function(f)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    result = checkFunction(expr, x)
    
    if result == None:
     
        simmetria = symmetries(expr)
        
        return {
            "msg": simmetria,
        }
    else:
        return result
