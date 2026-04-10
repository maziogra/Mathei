from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from account.entities.User import User
from account.Utils.getDb import get_db
import bcrypt
from account.Utils.getJWT import getJWT

router = APIRouter()

@router.get("/login")
async def login(
    email: str,
    password: str | None = None,
    db: Session = Depends(get_db)
):
    stmt = select(User).where(User.email == email)
    result = db.scalars(stmt).first()

    if not result:
        return {"error": "User not found"}

    if bcrypt.checkpw(password.encode(), result.password.encode()):
        token = getJWT({"id": result.id, "mail": result.email})
        return {"msg": "ok", "token": token}
    else:
        return {"error": "Wrong password"}