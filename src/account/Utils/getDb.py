from sqlalchemy.orm import Session
from account.main import engine

def get_db():
    with Session(engine) as session:
        yield session