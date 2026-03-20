from fastapi import APIRouter
import sympy as sp
from Symmetries.Symmetries import symmetries
from Utils.checkFunction import checkFunction

router = APIRouter()

@router.get("/symmetries")
async def get_symmetries(f: str | None = None):
    x = sp.symbols("x")
    f = sp.parse_expr(f, local_dict={"x": x}, evaluate=True)
    result = checkFunction(f, x)
    
    if result == None:
     
        simmetria = symmetries(f)
        
        return {
            "msg": "OK",
            "symmetry": simmetria,
        }
    else:
        return result
