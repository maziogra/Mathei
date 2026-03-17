from fastapi import APIRouter
import sympy as sp
from Sign.createSign import createSign

router = APIRouter()

@router.get("/sign")
async def get_sign(f: str | None = None):
    if f == None:
        return {"msg": "No function was provided"}
    
    else:
        x = sp.symbols("x")
        expr = sp.parse_expr(f, evaluate=True)

        if str(expr) == "zoo":
            return {"msg": "Division by zero"}
        
        for i in expr.free_symbols:
            if i != x:
                return {"msg": "Function is not correctly formatted"}
        
        intervals, signs = createSign(expr, x)
        
        signs_intervals = []
        for i in range(len(signs)):
            signs_intervals.append((str(intervals[i]), str(intervals[i+1]), signs[i]))
        
        return {
            "msg": "OK",
            "signs_intervals": signs_intervals,
        }