from abc import ABC, abstractmethod
from typing import List, Optional

from .book import Book


class BookRepository(ABC):
    @abstractmethod
    def select_by_isbn(self, isbn: str) -> Optional[Book]:
        raise NotImplementedError

    @abstractmethod
    def select_all_order_by_isbn(self) -> List[Book]:
        raise NotImplementedError

    @abstractmethod
    def insert(self, book: Book) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, book: Book) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete_by_isbn(self, isbn: str) -> None:
        raise NotImplementedError
