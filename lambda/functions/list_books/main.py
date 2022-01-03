import json
import os

from mt_sample_usecase.book_query_service import BookQueryService


def handler(event: dict, context: dict) -> dict:
    print(event)

    rds_host = os.environ.get("RDS_HOST")
    rds_user = os.environ.get("RDS_USER")
    rds_password = os.environ.get("RDS_PASSWORD")
    rds_database = os.environ.get("RDS_DATABASE")
    db_url = f"postgresql://{rds_user}:{rds_password}@{rds_host}/{rds_database}"

    try:
        query_service = BookQueryService(db_url)
        books = query_service.select_books_order_by_isbn()
        response = [book.to_dict() for book in books]
        return {
            "statusCode": 200,
            "body": json.dumps(response, ensure_ascii=False)
        }
    except Exception as e:
        print(e)
        return {
            "statusCode": 500,
            "body": json.dumps("ERROR")
        }
