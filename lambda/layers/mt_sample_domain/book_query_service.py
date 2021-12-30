from typing import List, Optional

from mt_sample_database.book_repository import BookRepositoryImpl
from mt_sample_database.database import Database

from .book import Book


class BookQueryService:
    def __init__(self, url: str):
        self._session = Database(url).get_session()

    def select_book_by_isbn(self, isbn: str) -> Optional[Book]:
        repository = BookRepositoryImpl(self._session)
        return repository.select_by_isbn(isbn)

    def select_books_order_by_isbn(self) -> List[Book]:
        repository = BookRepositoryImpl(self._session)
        return repository.select_all_order_by_isbn()

    def save_book(self, book: Book) -> Optional[Book]:
        repository = BookRepositoryImpl(self._session)
        book_from_db = repository.select_by_isbn(book.isbn)
        try:
            if book_from_db:
                repository.update(book)
            else:
                repository.insert(book)
            self._session.commit()
            return book
        except Exception as e:
            self._session.rollback()
            raise e
