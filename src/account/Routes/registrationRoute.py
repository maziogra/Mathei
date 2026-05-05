from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from account.entities.User import User
from account.Utils.getDb import get_db
from account.Utils.LoginRequest import LoginRequest
import bcrypt

router = APIRouter()

@router.post("/registration")
async def login(
    user: LoginRequest,
    db: Session = Depends(get_db)
):
    results = select(User).where(user.email == User.email)
    result = db.scalars(results).first()
    if result:
        raise HTTPException(status_code=400, detail="Already registered email")
    
    if not user.password:
        raise HTTPException(status_code=400, detail="No password provided")

    pswHash = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())

    userdb = User(id=0, email=user.email, password=pswHash)

    db.add(userdb)
    db.commit()
    return {"msg": "user created succesfully"}