from fastapi import APIRouter, HTTPException
import sympy as sp
from core.Intercepts.intersections import intersections
from core.Utils.checkFunction import checkFunction
from core.Utils.parseFunction import parse_function

router = APIRouter()

@router.get("/intersections")
async def get_intersections(f: str | None = None):
    x = sp.symbols("x")
    try:
        expr = parse_function(f)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    result = checkFunction(expr, x)
    
    if result == None:
        result = intersections(expr)
        
        punti = []
        for item in result:
            if not isinstance(item, str):
                punti.append(str(item))
            else:
                punti.append(item)
        
        if not punti:            
            return {
                "msg": "Nessun punto di intersezione trovato."
            }
        else:
            return {
                "msg": punti
            }
    else:
        return result