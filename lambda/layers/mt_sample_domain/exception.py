class BookNotFoundException(Exception):
    def __init__(self, isbn: str):
        self.isbn = isbn

    def __str__(self):
        return f"The book (isbn={self.isbn}) is not found"
