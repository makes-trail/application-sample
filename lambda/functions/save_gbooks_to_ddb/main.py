import os
import requests
import json
import boto3
from mt_sample_common import integration_response


# 取得したjsonデータから項目を挿入するための構造に整形
def format_gbooks(isbn: str, gbooks_json: dict) -> dict:
    if gbooks_json["totalItems"] != 1:
        print("The data fetched from GoogleBooks is empty")
        return {}
    output_dict = gbooks_json["items"][0]["volumeInfo"]
    output_dict["isbn"] = isbn
    output_dict["source"] = "gbooks"
    print(output_dict)
    return output_dict

def handler(event: dict, context: dict) -> dict:
    print(event)

    table_name = os.environ.get("DYNAMODB_TABLE")

    try:
        isbn = event.get("pathParameters").get("isbn")
        gbooks_api_url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
        headers = {"content-type": "application/json"}
        res = requests.get(gbooks_api_url, headers=headers, timeout=10.0)
        data = res.json()
        gbooks_dict = format_gbooks(isbn, data)
        
        if len(gbooks_dict) == 0:
            return integration_response.map(204)
        else:
            dynamo = boto3.resource("dynamodb")
            table = dynamo.Table(table_name)
            table.put_item(
                Item=gbooks_dict
            )
            return integration_response.map(200, json.dumps(gbooks_dict))
    except Exception as e:
        print(e)
        return integration_response.map(500, json.dumps("ERROR"))
