from fastapi import APIRouter
import sympy as sp

router = APIRouter()

@router.get("/derivatives")
async def get_derivatives(f: str | None = None):
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
        
        derivative = sp.diff(expr, x)
        
        return {
            "msg": "OK",
            "derivative": str(derivative),
        }