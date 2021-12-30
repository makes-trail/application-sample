from mt_sample_domain.exception import DatabaseConnectionException
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()


class Database:
    def __init__(self, url: str) -> None:
        self._engine = create_engine(url, connect_args={"connect_timeout": 10})

    def get_session(self) -> scoped_session:
        try:
            return scoped_session(sessionmaker(self._engine))
        except Exception as e:
            raise DatabaseConnectionException(e)
