from logging import getLogger
from typing import List, Optional

from mt_sample_domain.book import Book
from mt_sample_domain.book_repository import BookRepository
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.exc import NoResultFound

from .book_dto import BookDTO

logger = getLogger(__name__)


class BookRepositoryImpl(BookRepository):
    def __init__(self, session: scoped_session):
        self._session = session

    def select_by_isbn(self, isbn: str) -> Optional[Book]:
        try:
            book_dto = self._session.query(BookDTO).filter_by(isbn=isbn).one()
        except NoResultFound:
            return None
        except Exception:
            logger.exception("An unexcepted error occurred")
            raise
        return book_dto.to_entity()

    def select_all_order_by_isbn(self) -> List[Book]:
        try:
            book_dto_list = self._session.query(BookDTO).order_by(BookDTO.isbn).all()
        except NoResultFound:
            return []
        except Exception:
            logger.exception("An unexcepted error occurred")
            raise
        return [dto.to_entity() for dto in book_dto_list]

    def insert(self, book: Book) -> None:
        book_dto = BookDTO.from_entity(book)
        try:
            self._session.add(book_dto)
        except Exception:
            logger.exception("An unexcepted error occurred")
            raise

    def update(self, book: Book) -> None:
        book_dto = BookDTO.from_entity(book)
        try:
            _book = self._session.query(BookDTO).filter_by(isbn=book_dto.isbn).one()
            _book.title = book_dto.title
            _book.author = book_dto.author
            _book.publisher = book_dto.publisher
            _book.cover = book_dto.cover
        except Exception:
            logger.exception("An unexcepted error occurred")
            raise

    def delete_by_isbn(self, isbn: str) -> None:
        try:
            self._session.query(BookDTO).filter_by(isbn=isbn).delete()
        except Exception:
            logger.exception("An unexcepted error occurred")
            raise
