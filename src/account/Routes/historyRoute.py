from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from account.entities.User import User
from account.Utils.getDb import get_db
from account.Utils.verifyJWT import verifyJWT

router = APIRouter()

@router.post("/history")
async def postHistory(
    f: str,
    payload=Depends(verifyJWT),
    db: Session = Depends(get_db)
):
    print(payload.id, "-------", f)
    return {"msg": "ok"}