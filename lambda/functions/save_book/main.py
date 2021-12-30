import json
import os

from mt_sample_domain.book import Book
from mt_sample_domain.book_query_service import BookQueryService


def handler(event: dict, context: dict) -> dict:
    print(event)

    rds_host = os.environ.get("RDS_HOST")
    rds_user = os.environ.get("RDS_USER")
    rds_password = os.environ.get("RDS_PASSWORD")
    rds_database = os.environ.get("RDS_DATABASE")
    db_url = f"postgresql://{rds_user}:{rds_password}@{rds_host}/{rds_database}"

    body: dict = json.loads(event["body"])
    try:
        book = Book.from_dict(body)
        query_service = BookQueryService(db_url)
        saved_book = query_service.save_book(book)
        return {
            "statusCode": 200,
            "body": json.dumps(saved_book.to_dict(), ensure_ascii=False)
        }
    except Exception as e:
        print(e)
        return {
            "statusCode": 500,
            "body": json.dumps("ERROR")
        }
