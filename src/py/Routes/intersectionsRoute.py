from fastapi import APIRouter
import sympy as sp
from Intercepts.intersections import intersections

router = APIRouter()

@router.get("/intersections")
async def get_intersections(f: str | None = None):
    if f == None:
        return {"msg": "No function was provided"}
    
    else:
        x = sp.symbols("x")
        expr = sp.parse_expr(f, local_dict={"x": x}, evaluate=True)

        if str(expr) == "zoo":
            return {"msg": "Division by zero"}
        
        for i in expr.free_symbols:
            if i != x:
                return {"msg": "Function is not correctly formatted"}
        
        result = intersections(expr)
        
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