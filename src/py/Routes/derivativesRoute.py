from fastapi import APIRouter
import sympy as sp
from Utils.checkFunction import checkFunction

router = APIRouter()

@router.get("/derivatives")
async def get_derivatives(f: str | None = None):
    x = sp.symbols("x")
    f = sp.parse_expr(f, local_dict={"x": x}, evaluate=True)
    result = checkFunction(f, x)
    
    if result == None:
        derivative = sp.diff(f, x)
        
        return {
            "msg": "OK",
            "derivative": str(derivative),
        }
    else:
        return result