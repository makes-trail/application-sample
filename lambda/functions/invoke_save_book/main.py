import os
import requests
import json
import boto3

from mt_sample_common.entity import Book
from mt_sample_common import integration_response


def handler(event: dict, context: dict) -> dict:
    print(event)

    child_function_name = os.environ.get("CHILD_FUNCTION_NAME")

    try:
        isbn = event.get("pathParameters").get("isbn")
        payload = {
            "isbn": isbn
        }
        client = boto3.client("lambda")
        response = client.invoke(
            FunctionName=child_function_name,
            InvocationType="RequestResponse",
            LogType="Tail",
            Payload=json.dumps(payload)
        )
        response_json = json.loads(response["Payload"].read())
        if response_json["status"] == "success":
            book = response_json["book"]
            if book:
                return integration_response.map(200, json.dumps(book, ensure_ascii=False))
            else:
                return integration_response.map(204)
        else:
            return integration_response.map(500, json.dumps("ERROR"))
    except Exception as e:
        print(e)
        return integration_response.map(500, json.dumps("ERROR"))
