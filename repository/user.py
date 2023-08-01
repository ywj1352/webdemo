from sqlalchemy import Column, String, Integer

from . import DBSession as session
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer(), primary_key=True)
    username = Column(String(50), unique=False, nullable=True)
    password = Column(String(100), unique=False, nullable=True)
    name = Column(String(100), unique=False, nullable=True)
    avatar = Column(String(100), unique=False, nullable=True)
    telephone = Column(String(20), unique=False, nullable=True)
    email = Column(String(100), unique=False, nullable=True)
    location = Column(String(100), unique=False, nullable=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


def get_account(id: int):
    session().query(Account).filter(Account.id == id).one()
