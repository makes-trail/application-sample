import json

from mt_sample_domain.book import Book
from mt_sample_domain.exception import BookNotFoundException


def handler(event: dict, context: dict) -> dict:
    print(event)

    isbn: str = event["pathParameters"]["isbn"]
    try:
        book = Book.search_by_isbn(isbn)
        response = [book.to_dict()]
        return {
            "statusCode": 200,
            "body": json.dumps(response, ensure_ascii=False)
        }
    except BookNotFoundException as e:
        print(e)
        return {
            "statusCode": 200,
            "body": json.dumps([], ensure_ascii=False)
        }
    except Exception as e:
        print(e)
        return {
            "statusCode": 500,
            "body": json.dumps("ERROR")
        }
