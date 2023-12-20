import datetime
from uuid import UUID

from sqlalchemy import Integer, ForeignKey, Column, String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.dialects.sqlite import DATETIME

from LocalStorageService.Connection import engine


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    password = Column(String)
    auth_key = Column(String)
    privilege = Column(Boolean)


class Pools(Base):
    __tablename__ = "pools"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pool_name = Column(String, unique=True)
    pool_uniq_id = Column(String, unique=True)
    created_a = Column(DATETIME, default=datetime.datetime.now)

    connections = relationship(
        "Connections",
        back_populates="pool"
    )


class Connections(Base):
    __tablename__ = "connections"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pool_id = Column(ForeignKey("pools.id", ondelete="CASCADE"))
    connection_url = Column(String)
    name = Column(String, unique=True)
    description = Column(String)

    pool = relationship(
        "Pools",
        back_populates="connections"
    )


def create_all():
    Base.metadata.create_all(bind=engine)