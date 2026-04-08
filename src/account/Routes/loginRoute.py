from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from account.entities.User import User
from account.Utils.getDb import get_db
import bcrypt

router = APIRouter()

@router.get("/login")
async def login(
    username: str,
    password: str | None = None,
    db: Session = Depends(get_db)
):
    stmt = select(User).where(User.username == username)
    result = db.scalars(stmt).first()

    if not result:
        return {"error": "User not found"}

    if bcrypt.checkpw(password.encode(), result.password.encode()):
        return {"msg": "ok"}
    else:
        return {"error": "Wrong password"}