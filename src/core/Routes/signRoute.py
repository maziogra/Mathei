from fastapi import APIRouter
import sympy as sp
from core.Sign.createSign import createSign
from core.Utils.checkFunction import checkFunction

router = APIRouter()

@router.get("/sign")
async def get_sign(f: str | None = None):
    x = sp.symbols("x")
    f = sp.parse_expr(f, local_dict={"x": x}, evaluate=True)
    result = checkFunction(f, x)
    
    if result == None:
        intervals, signs, warning = createSign(f, x)
        
        signs_intervals = []
        for i in range(len(signs)):
            signs_intervals.append((str(intervals[i]), str(intervals[i+1]), signs[i]))
        
        return {
            "msg": "OK",
            "signs_intervals": signs_intervals,
            "warning": warning,
        }
    else:
        return result