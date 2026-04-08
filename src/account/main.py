from sqlalchemy import create_engine
from account.entities.Base import Base
from account.entities.Function import Function
from account.entities.User import User

engine = create_engine(
    "mysql+pymysql://root:root@localhost:3306/mathei",
    echo=True
)

Base.metadata.create_all(engine)