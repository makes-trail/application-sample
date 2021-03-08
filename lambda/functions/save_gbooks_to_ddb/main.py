import os
import requests
import boto3
import json


# 取得したjsonデータから項目を挿入するための構造に整形
def format_gbooks(isbn: str, gbooks_json: dict) -> dict:
    if gbooks_json["totalItems"] != 1:
        print("The data fetched from GoogleBooks is empty")
        raise
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
    
        dynamo = boto3.resource("dynamodb")
        table = dynamo.Table(table_name)
        table.put_item(
            Item=gbooks_dict
        )

        return {
            "statusCode": 204,
            "headers": {
              "Access-Control-Allow-Headers": "Content-Type",
              "Access-Control-Allow-Origin": "*",
              "Access-Control-Allow-Methods": "*"
            }
        }
    except Exception as e:
        print(e)
        return {
            "statusCode": 500,
            "headers": {
              "Access-Control-Allow-Headers": "Content-Type",
              "Access-Control-Allow-Origin": "*",
              "Access-Control-Allow-Methods": "*"
            },
            "body": json.dumps("ERROR")
        }
