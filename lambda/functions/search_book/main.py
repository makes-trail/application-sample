import json

from mt_sample_domain.book import Book
from mt_sample_domain.exception import BookNotFoundException
from mt_sample_interface.log import get_logger


def handler(event: dict, context: dict) -> dict:
    logger = get_logger(__name__)
    logger.info(event)

    isbn: str = event["pathParameters"]["isbn"]
    try:
        book = Book.search_by_isbn(isbn)
        response = [book.to_dict()]
        return {"statusCode": 200, "body": json.dumps(response, ensure_ascii=False)}
    except BookNotFoundException as e:
        logger.info(e)
        return {"statusCode": 200, "body": json.dumps([], ensure_ascii=False)}
    except Exception:
        logger.exception("An unexcepted error occurred while searching book")
        return {"statusCode": 500, "body": json.dumps("ERROR")}
