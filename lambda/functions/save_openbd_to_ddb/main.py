import os
import requests
import boto3
import json


# 取得したjsonデータから項目を挿入するための構造に整形
def format_openbd(isbn: str, openbd_json: dict) -> dict:
    if len(openbd_json) != 1:
        print("The data fetched from OpenBD is empty")
        raise
    output_dict = openbd_json[0]["summary"]
    output_dict["isbn"] = isbn
    output_dict["source"] = "openbd"
    print(output_dict)
    return output_dict

def handler(event: dict, context: dict) -> dict:
    print(event)

    table_name = os.environ.get("DYNAMODB_TABLE")

    try:
        isbn = event.get("pathParameters").get("isbn")
        openbd_api_url = f"https://api.openbd.jp/v1/get?isbn={isbn}"
        headers = {"content-type": "application/json"}
        res = requests.get(openbd_api_url, headers=headers, timeout=10.0)
        data = res.json()
        openbd_dict = format_openbd(isbn, data)
    
        dynamo = boto3.resource("dynamodb")
        table = dynamo.Table(table_name)
        table.put_item(
            Item=openbd_dict
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