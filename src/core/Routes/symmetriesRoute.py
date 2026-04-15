from fastapi import APIRouter
import sympy as sp
from core.Symmetries.Symmetries import symmetries
from core.Utils.checkFunction import checkFunction

router = APIRouter()

@router.get("/symmetries")
async def get_symmetries(f: str | None = None):
    x = sp.symbols("x")
    f = sp.parse_expr(f, local_dict={"x": x}, evaluate=True)
    result = checkFunction(f, x)
    
    if result == None:
     
        simmetria = symmetries(f)
        
        return {
            "msg": simmetria,
        }
    else:
        return result
