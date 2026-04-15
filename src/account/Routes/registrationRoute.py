from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from account.entities.User import User
from account.Utils.getDb import get_db
import bcrypt

router = APIRouter()

@router.post("/registration")
async def login(
    email: str,
    password: str | None = None,
    db: Session = Depends(get_db)
):
    results = select(User).where(email == User.email)
    result = db.scalars(results).first()
    if result:
        raise HTTPException(status_code=400, detail="Already registered email")
    
    if not password:
        raise HTTPException(status_code=400, detail="No password provided")

    pswHash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    user = User(id=0, email=email, password=pswHash)

    db.add(user)
    db.commit()
    return {"msg": "user created succesfully"}