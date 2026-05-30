from fastapi import APIRouter, HTTPException
import sympy as sp
from core.Sign.createSign import createSign
from core.Utils.checkFunction import checkFunction
from core.Utils.parseFunction import parse_function

router = APIRouter()

@router.get("/sign")
async def get_sign(f: str | None = None):
    x = sp.symbols("x")
    try:
        expr = parse_function(f)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    result = checkFunction(expr, x)
    
    if result == None:
        intervals, signs, warning = createSign(expr, x)
        
        signs_intervals = []
        for i in range(len(signs)):
            signs_intervals.append((str(intervals[i]), str(intervals[i+1]), signs[i]))
        
        return {
            "msg": signs_intervals,
            "warning": warning,
        }
    else:
        return result