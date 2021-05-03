import os
import json
import psycopg2
from psycopg2.extras import RealDictCursor
import boto3

from mt_sample_common.entity import Book
from mt_sample_common import integration_response


def handler(event: dict, context: dict) -> dict:
    print(event)

    rds_host = os.environ.get("RDS_HOST")
    rds_user = os.environ.get("RDS_USER")
    rds_password = os.environ.get("RDS_PASSWORD")
    rds_database = os.environ.get("RDS_DATABASE")
    dsn = f"host={rds_host} user={rds_user} password={rds_password} dbname={rds_database}"

    # Booksテーブルに存在する書籍一覧をisbn昇順で取得する
    sql_get_all_books = """
        SELECT isbn, title, author, publisher, cover
        FROM books
        ORDER BY isbn"""

    try:
        with psycopg2.connect(dsn) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(sql_get_all_books)
                rows = cur.fetchall()
        
        book_list = [Book(row["isbn"], row["title"], row["author"], row["publisher"], row["cover"]) for row in rows]
        response = [book.__dict__ for book in book_list]

        return integration_response.map(200, json.dumps(response, ensure_ascii=False))
    except Exception as e:
        print(e)
        return integration_response.map(500, json.dumps("ERROR"))
