from typing import List, Optional

from mt_sample_database.book_datasource import BookDatasource
from mt_sample_database.database import Database
from mt_sample_domain.book import Book
from mt_sample_domain.exception import BookNotFoundException


class BookService:
    def __init__(self, url: str):
        self._session = Database(url).get_session()

    def search_book_by_isbn(self, isbn: str) -> Optional[Book]:
        book_from_db = self.select_book_by_isbn(isbn)
        if book_from_db:
            return book_from_db
        try:
            return Book.search_by_isbn(isbn)
        except BookNotFoundException as e:
            raise e

    def select_book_by_isbn(self, isbn: str) -> Optional[Book]:
        datasource = BookDatasource(self._session)
        return datasource.select_by_isbn(isbn)

    def select_books_order_by_isbn(self) -> List[Book]:
        datasource = BookDatasource(self._session)
        return datasource.select_all_order_by_isbn()

    def save_book(self, book: Book) -> Optional[Book]:
        datasource = BookDatasource(self._session)
        book_from_db = datasource.select_by_isbn(book.isbn)
        try:
            if book_from_db:
                datasource.update(book)
            else:
                datasource.insert(book)
            self._session.commit()
            return book
        except Exception as e:
            self._session.rollback()
            raise e
