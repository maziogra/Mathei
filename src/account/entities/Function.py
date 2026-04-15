from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from account.entities.Base import Base

class Function(Base):
    __tablename__ = "functions"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    function: Mapped[str] = mapped_column(String(250))

    def __repr__(self) -> str:
        return f"Function(id={self.id!r}, user_id={self.user_id!r}, function={self.function!r})"