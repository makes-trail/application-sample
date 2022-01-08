from logging import getLogger
from typing import Final, List, Optional

import requests

logger = getLogger(__name__)


class GoogleApiBook:
    api_endpoint: Final[str] = "https://www.googleapis.com/books/v1"

    def __init__(
        self, isbn: str, title: str, subtitle: str, authors: List[str], thumbnail: str
    ) -> None:
        self.isbn = isbn
        self.title = title
        self.subtitle = subtitle
        self.authors = authors
        self.thumbnail = thumbnail

    @classmethod
    def search_by_isbn(cls, isbn: str) -> Optional["GoogleApiBook"]:
        url = f"{cls.api_endpoint}/volumes?q=isbn:{isbn}"
        headers = {"content-type": "application/json"}
        try:
            res = requests.get(url, headers=headers, timeout=10.0)
            data = res.json()
            logger.info(data)
        except Exception as e:
            logger.exception("Failed to fetch data from openBD API")
            raise e

        if data["totalItems"] == 0:
            return None
        else:
            volume_info = data["items"][0]["volumeInfo"]
            title = volume_info["title"]
            subtitle = volume_info.get("subttitle", "")
            authors = volume_info.get("authors", "")
            thumbnail = ""
            if volume_info.get("imageLinks") is not None:
                thumbnail = volume_info["imageLinks"].get("thumbnail", "")
            return cls(
                isbn,
                title,
                subtitle,
                authors,
                thumbnail,
            )
