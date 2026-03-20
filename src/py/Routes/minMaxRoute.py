from fastapi import APIRouter
import sympy as sp
from Utils.checkFunction import checkFunction
from minMax.minMax import minMax

router = APIRouter()

@router.get("/minMax")
async def get_intersections(f: str | None = None):
    x = sp.symbols("x")
    f = sp.parse_expr(f, local_dict={"x": x}, evaluate=True)
    result = checkFunction(f, x)
    
    if result == None:
        punti = minMax(f, x) 
        
        return {
            "msg": "OK",
            "punti": str(punti),
        }
    else:
        return result
