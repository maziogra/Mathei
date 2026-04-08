from fastapi import APIRouter
import sympy as sp
from core.Intercepts.intersections import intersections
from core.Utils.checkFunction import checkFunction

router = APIRouter()

@router.get("/intersections")
async def get_intersections(f: str | None = None):
    x = sp.symbols("x")
    f = sp.parse_expr(f, local_dict={"x": x}, evaluate=True)
    result = checkFunction(f, x)
    
    if result == None:
        result = intersections(f)
        
        punti = []
        for item in result:
            if not isinstance(item, str):
                punti.append(str(item))
            else:
                punti.append(item)
        
        return {
            "msg": "OK",
            "punti": punti,
        }
    else:
        return result