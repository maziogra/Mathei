from fastapi import APIRouter
import sympy as sp
from Domain.domain import domain

router = APIRouter()

@router.get("/domain")
async def get_domain(f: str | None = None):
    if f == None:
        return {"msg": "No function was provided"}
    
    else:
        x = sp.symbols('x')
        #expr = sp.parse_expr(f, evaluate=True)
        expr = sp.parse_expr(f, evaluate=True) 
        if str(expr) == "zoo":
            return {"msg": "Division by zero"}
        
        for i in expr.free_symbols:
            if i != x:
                return {"msg": "Function is not correctly formatted"}
        dominio = sp.pretty(domain(expr,x))

        return {
            "msg": "OK",
            "domain": str(dominio),
        }
    