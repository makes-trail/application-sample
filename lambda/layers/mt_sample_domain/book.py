from .exception import BookNotFoundException
from .google_api import GoogleApiBook
from .openbd import OpenbdBook


class Book:
    def __init__(
        self, isbn: str, title: str, author: str, publisher: str, cover: str
    ) -> None:
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.cover = cover

    def serialize(self) -> dict:
        return self.__dict__

    @classmethod
    def search_by_isbn(cls, isbn: str) -> "Book":
        try:
            open_bd_book = OpenbdBook.search_by_isbn(isbn)
            google_api_book = GoogleApiBook.search_by_isbn(isbn)
        except Exception as e:
            raise e

        if open_bd_book is None:
            if google_api_book is None:
                raise BookNotFoundException(isbn)
            else:
                return cls._convert_google_api_to_book(google_api_book)
        else:
            if google_api_book is None:
                return cls._convert_openbd_to_book(open_bd_book)
            else:
                return cls._convert_both_to_book(open_bd_book, google_api_book)

    @classmethod
    def _convert_openbd_to_book(cls, openbd_book: OpenbdBook) -> "Book":
        return cls(
            openbd_book.isbn,
            openbd_book.title,
            openbd_book.author,
            openbd_book.publisher,
            openbd_book.cover,
        )

    @classmethod
    def _convert_google_api_to_book(cls, google_api_book: GoogleApiBook) -> "Book":
        isbn = google_api_book.isbn
        title = google_api_book.title
        author = " ".join(google_api_book.authors)
        publisher = ""
        cover = google_api_book.thumbnail
        return cls(isbn, title, author, publisher, cover)

    @classmethod
    def _convert_both_to_book(
        cls, openbd_book: OpenbdBook, google_api_book: GoogleApiBook
    ) -> "Book":
        isbn = openbd_book.isbn
        title = openbd_book.title if openbd_book.title != "" else google_api_book.title
        author = (
            openbd_book.author
            if openbd_book.author != ""
            else " ".join(google_api_book.authors)
        )
        publisher = openbd_book.publisher
        cover = (
            openbd_book.cover if openbd_book.cover != "" else google_api_book.thumbnail
        )
        return cls(isbn, title, author, publisher, cover)
