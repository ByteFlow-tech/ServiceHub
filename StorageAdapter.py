import asyncio

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session


class StorageAdapter:
    class Base(DeclarativeBase):
        pass

    class ConnectedServices(Base):
        __tablename__ = "connected_services"

        id = Column(Integer, primary_key=True, autoincrement=True)
        service_name = Column(String, nullable=False)
        service_host = Column(String, nullable=False)
        service_port = Column(Integer, nullable=False)

    def __init__(self):
        self._sync_engine = create_engine("sqlite:///storage.db")
        self.Base.metadata.create_all(bind=self._sync_engine)

    def add_connection(
            self,
            service_name,
            service_host,
            service_port
    ):
        new_conn = self.ConnectedServices(
            service_name=service_name,
            service_host=service_host,
            service_port=service_port
        )
        with Session(autoflush=False, bind=self._sync_engine) as db:
            db.add(new_conn)
            db.commit()
