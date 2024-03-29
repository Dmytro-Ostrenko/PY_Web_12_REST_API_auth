from sqlalchemy import orm
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import DeclarativeBase



class Base(orm.DeclarativeBase):
    pass

class Contact(Base):
    __tablename__ = "contacts"   
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    first_name: orm.Mapped[str] = orm.mapped_column(String(20), nullable=False)
    last_name: orm.Mapped[str] = orm.mapped_column(String(20), nullable=False)
    email: orm.Mapped[str] = orm.mapped_column(String(50), nullable=False)
    phone_number: orm.Mapped[str] = orm.mapped_column(String(13), nullable=False)
    birthday: orm.Mapped[str] = orm.mapped_column(Date, nullable=False)
    additional_info: orm.Mapped[str] = orm.mapped_column(String(200))