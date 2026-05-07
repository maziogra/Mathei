from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from account.entities.User import User
from account.Utils.getDb import get_db
import bcrypt
from account.Utils.getJWT import getJWT
from account.Utils.LoginRequest import LoginRequest

router = APIRouter()

@router.post("/login")
async def login(
    user: LoginRequest,
    db: Session = Depends(get_db)
):
    stmt = select(User).where(User.email == user.email)
    result = db.scalars(stmt).first()
    
    if not result:
        raise HTTPException(status_code=400, detail="User not found")

    if bcrypt.checkpw(user.password.encode(), result.password.encode()):
        token = getJWT({"id": result.id, "mail": result.email})
        return {"token": token}
    else:
        raise HTTPException(status_code=400, detail="Wrong password")