import requests
import json

from mt_sample_common.entity import Book
from mt_sample_common import integration_response


def handler(event: dict, context: dict) -> dict:
    print(event)

    try:
        isbn = event.get("pathParameters").get("isbn")
        openbd_api_url = f"https://api.openbd.jp/v1/get?isbn={isbn}"
        headers = {"content-type": "application/json"}
        res = requests.get(openbd_api_url, headers=headers, timeout=10.0)
        data = res.json()
        
        response = []
        if data:
            if data[0] is not None:
                summary = data[0]["summary"]
        
                summary_isbn = summary["isbn"]
                summary_title = summary["title"]
                summary_author = summary["author"]
                summary_publisher = summary["publisher"]
                summary_cover = summary["cover"]
        
                book = Book(summary_isbn, summary_title, summary_author, summary_publisher, summary_cover)
                response.append(book.__dict__)

        return integration_response.map(200, json.dumps(response, ensure_ascii=False))
    except Exception as e:
        print(e)
        return integration_response.map(500, json.dumps("ERROR"))
