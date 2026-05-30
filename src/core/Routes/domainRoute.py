from fastapi import APIRouter, HTTPException
import sympy as sp
from core.Domain.domain import domain
from core.Utils.checkFunction import checkFunction
from core.Utils.parseFunction import parse_function

router = APIRouter()

@router.get("/domain")
async def get_domain(f: str | None = None):
    x = sp.symbols("x")
    try:
        expr = parse_function(f)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    result = checkFunction(expr, x)
    
    if result == None:
        dominio = sp.pretty(domain(expr, x))

        return {
            "msg": str(dominio)
        }
    else:
        return result
    