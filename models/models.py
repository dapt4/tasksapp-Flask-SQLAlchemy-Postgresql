from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String

class Base(DeclarativeBase):
    pass



class Task(Base):
    __tablename__ = "task"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(200))

    def to_dict(self):
        return {"id": self.id, "title": self.title, "description": self.description }
    def __repr__(self) -> str:
        return f'Task(id={self.id}, title={self.title}, description={self.description})'
