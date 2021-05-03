from dataclasses import dataclass 

@dataclass
class Book:
    isbn: str
    title: str
    author: str
    publisher: str
    cover: str
