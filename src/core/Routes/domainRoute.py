from fastapi import APIRouter
import sympy as sp
from core.Domain.domain import domain
from core.Utils.checkFunction import checkFunction

router = APIRouter()

@router.get("/domain")
async def get_domain(f: str | None = None):
    x = sp.symbols("x")
    f = sp.parse_expr(f, local_dict={"x": x}, evaluate=True)
    result = checkFunction(f, x)
    
    if result == None:
        dominio = sp.pretty(domain(f,x))

        return {
            "msg": str(dominio)
        }
    else:
        return result
    