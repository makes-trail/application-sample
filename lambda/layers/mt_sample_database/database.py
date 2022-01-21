from logging import getLogger

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

logger = getLogger(__name__)

Base = declarative_base()


class Database:
    def __init__(self, url: str) -> None:
        self._url = url

    def get_session(self) -> scoped_session:
        try:
            engine = create_engine(self._url, connect_args={"connect_timeout": 10})
            return scoped_session(sessionmaker(engine))
        except Exception:
            logger.exception("Could not connect to database")
            raise
