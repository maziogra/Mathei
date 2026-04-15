from fastapi import APIRouter
import sympy as sp
from core.Utils.checkFunction import checkFunction
from core.Asymptotes.asymptotes import asymptotes

router = APIRouter()

@router.get("/asymptotes")
async def get_asymptotes(f: str | None = None):
    x = sp.symbols("x")
    f = sp.parse_expr(f, local_dict={"x": x}, evaluate=True)
    result = checkFunction(f, x)
    
    if result == None:
        asintoti, warning = asymptotes(f, x)
        
        return {
            "msg": str(asintoti),
            "warning": warning
        }
    else:
        return result