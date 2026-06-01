from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, Any
from pymysql import IntegrityError
from sqlalchemy import select
from sqlalchemy.orm import Session
from account.entities.Function import Function
from account.Utils.getDb import get_db
from account.Utils.verifyJWT import verifyJWT
from fastapi import Body

router = APIRouter()

@router.post("/history")
async def postHistory(
    data: Dict[str, Any] = Body(...),
    payload=Depends(verifyJWT),
    db: Session = Depends(get_db)
):
  
    f = Function(
        user_id=payload["id"],
        function=data["f"],
        latex=data["latex"]
    )

    try:
        db.add(f)
        db.commit()

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")
    
    return {"msg": "ok"}

@router.get("/history")
async def getHistory(
    elements: int = 10,
    offset: int = 0,
    payload=Depends(verifyJWT),
    db: Session = Depends(get_db)
):
    if elements > 25:
        elements = 25
    
    stmt = select(Function).where(Function.user_id == payload["id"]).limit(elements).offset(offset)
    result = db.scalars(stmt).all()
    
    return {"functions": result}

@router.delete("/history/{entry_id}")
async def delete_function(
    entry_id:     int,
    payload=Depends(verifyJWT),
    db: Session = Depends(get_db)
):
    entry = (
        db.query(Function)
        .filter(
            Function.id      == entry_id,
            Function.user_id == payload["id"],
        )
        .first()
    )
    if not entry:
        raise HTTPException(status_code=404, detail="Funzione non trovata")

    db.delete(entry)
    db.commit()
    return {"msg": "eliminata"}


@router.delete("/history")
async def delete_all_functions(
    payload=Depends(verifyJWT),
    db: Session = Depends(get_db)
):
    deleted_count = (
        db.query(Function)
        .filter(Function.user_id == payload["id"])
        .delete(synchronize_session=False)
    )
    db.commit()
    return {"msg": f"{deleted_count} funzioni eliminate"}