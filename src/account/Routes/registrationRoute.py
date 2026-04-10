from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from account.entities.User import User
from account.Utils.getDb import get_db
import bcrypt

router = APIRouter()

@router.get("/registration")
async def login(
    email: str,
    password: str | None = None,
    db: Session = Depends(get_db)
):
    results = select(User).where(email == User.email)
    result = db.scalars(results).first()
    if result:
        return {"error": "already registered email"}
    
    if not password:
        return {"error": "no password provided"}

    pswHash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    user = User(id=0, email=email, password=pswHash)

    db.add(user)
    db.commit()
    return {"msg": "user created succesfully"}