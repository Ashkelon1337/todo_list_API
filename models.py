from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import String, Boolean
from pydantic import BaseModel
class Todolist(Base):
    __tablename__ = 'todo_list'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(95))
    completed: Mapped[bool] = mapped_column(Boolean, default=False)

class TaskCreate(BaseModel):
    title: str

class TaskResponse(TaskCreate):
    id: int
    completed: bool

