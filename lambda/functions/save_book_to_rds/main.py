import os
import json
import psycopg2
import boto3
from mt_sample_common.entity import Book


# OpenBDのアイテムからBookエンティティの構造に変換
def convert_openbd_item_to_book(openbd_item: dict) -> "Book":
    isbn = openbd_item["isbn"]
    title = openbd_item["title"]
    author = openbd_item["author"]
    publisher = openbd_item["publisher"]
    cover = openbd_item["cover"]
    book = Book(isbn, title, author, publisher, cover)
    return book

# Google BooksのアイテムからBookエンティティの構造に変換
def convert_gbooks_item_to_book(gbooks_item: dict) -> "Book":
    isbn = gbooks_item["isbn"]
    title = gbooks_item["title"]
    author = " ".join(gbooks_item["authors"])
    publisher = gbooks_item["publisher"]
    cover = gbooks_item["imageLinks"]["thumbnail"]

    book = Book(isbn, title, author, publisher, cover)
    return book

# OpenBDとGoogle BooksのアイテムからBookエンティティの構造に変換
def convert_both_items_to_book(openbd_item: dict, gbooks_item: dict) -> "Book":
    isbn = openbd_item["isbn"]
    title = openbd_item["title"] if openbd_item["title"] != "" else gbooks_item["title"]
    author = openbd_item["author"] if openbd_item["author"] != "" else " ".join(gbooks_item["authors"])
    publisher = openbd_item["publisher"] if openbd_item["publisher"] != "" else gbooks_item["publisher"]
    cover = openbd_item["cover"] if openbd_item["cover"] != "" else gbooks_item["imageLinks"]["thumbnail"]

    book = Book(isbn, title, author, publisher, cover)
    return book

def handler(event: dict, context: dict) -> dict:
    print(event)

    table_name = os.environ.get("DYNAMODB_TABLE")
    rds_host = os.environ.get("RDS_HOST")
    rds_user = os.environ.get("RDS_USER")
    rds_password = os.environ.get("RDS_PASSWORD")
    rds_database = os.environ.get("RDS_DATABASE")
    dsn = f"host={rds_host} user={rds_user} password={rds_password} dbname={rds_database}"

    # 指定したISBNコードの書籍がBooksテーブルに存在するかチェックする
    sql_checkifexists = """
        SELECT COUNT(isbn)
        FROM books
        WHERE isbn = %(isbn)s"""
    # Booksテーブルに新しい書籍を追加する
    sql_insert = """
        INSERT INTO books(isbn, title, author, publisher, cover)
        VALUES (%(isbn)s, %(title)s, %(author)s, %(publisher)s, %(cover)s)"""
    # Booksテーブルで指定したISBNコードの書籍情報を更新する
    sql_update = """
        UPDATE books
        SET isbn = %(isbn)s,
            title = %(title)s,
            author = %(author)s,
            publisher = %(publisher)s,
            cover = %(cover)s
        WHERE isbn = %(isbn)s"""

    try:
        isbn = event.get("isbn")
        dynamo = boto3.resource("dynamodb")
        table = dynamo.Table(table_name)
        response_openbd = table.get_item(
            Key={"isbn": isbn, "source": "openbd"}
        )
        response_gbooks = table.get_item(
            Key={"isbn": isbn, "source": "gbooks"}
        )
        
        openbd_item = response_openbd.get("Item")
        gbooks_item = response_gbooks.get("Item")
        if openbd_item is None and gbooks_item is None:
            return {
                "status": "success",
                "book": ""
            }
        elif openbd_item is not None and gbooks_item is None:
            book = convert_openbd_item_to_book(openbd_item)
        elif openbd_item is None and gbooks_item is not None:
            book = convert_gbooks_item_to_book(gbooks_item)
        else:
            book = convert_both_items_to_book(openbd_item, gbooks_item)
        
        with psycopg2.connect(dsn) as conn:
            with conn.cursor() as cur:
                cur.execute(sql_checkifexists, {"isbn": book.isbn})
                (count,) = cur.fetchone()
        
        if count == 0:
            # 書籍が存在しない場合は追加
            with psycopg2.connect(dsn) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql_insert, book.__dict__)
                conn.commit()
        else:
            # 書籍がすでに存在する場合は更新
            with psycopg2.connect(dsn) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql_update, book.__dict__)
                conn.commit()

        return {
            "status": "success",
            "book": json.dumps(book.__dict__, ensure_ascii=False)
        }
    except Exception as e:
        print(e)
        return {
            "status": "error"
        }
