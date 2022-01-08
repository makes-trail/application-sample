from logging import getLogger
from typing import Final, Optional

import requests

logger = getLogger(__name__)


class OpenbdBook:
    api_endpoint: Final[str] = "https://api.openbd.jp/v1"

    def __init__(
        self, isbn: str, title: str, author: str, publisher: str, cover: str
    ) -> None:
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.cover = cover

    @classmethod
    def search_by_isbn(cls, isbn: str) -> Optional["OpenbdBook"]:
        url = f"{cls.api_endpoint}/get?isbn={isbn}"
        headers = {"content-type": "application/json"}
        try:
            res = requests.get(url, headers=headers, timeout=10.0)
            data = res.json()
            logger.info(data)
        except Exception as e:
            logger.exception("Failed to fetch data from openBD API")
            raise e

        if data[0] is None:
            return None
        else:
            summary = data[0]["summary"]
            summary_isbn = summary["isbn"]
            summary_title = summary["title"]
            summary_author = summary["author"]
            summary_publisher = summary["publisher"]
            summary_cover = summary["cover"]
            return cls(
                summary_isbn,
                summary_title,
                summary_author,
                summary_publisher,
                summary_cover,
            )
