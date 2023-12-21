from sqlalchemy import create_engine
from sqlalchemy.orm import Session


engine = create_engine("sqlite:///LocalStorageService/LocalStorage/storage.db", echo=False)


def get_db() -> Session:
    with Session(autoflush=False, bind=engine) as session:
        return session
