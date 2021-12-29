from sqlalchemy import Column, String

from mt_sample_database.database import Base
from mt_sample_domain.book import Book


class BookDTO(Base):
    __tablename__ = "book"
    isbn = Column(String(13), unique=True, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publisher = Column(String, nullable=False)
    cover = Column(String, nullable=False)

    def to_entity(self) -> Book:
        return Book(self.isbn, self.title, self.author, self.publisher, self.cover)

    @staticmethod
    def from_entity(book: Book) -> "BookDTO":
        return BookDTO(book.isbn, book.title, book.author, book.publisher, book.cover)
