'''
指定した項目を更新する。

rating属性を削除する。

[Notes] rating属性が存在していなくてもエラーは吐かれない。（そのままスルー。）
'''

from decimal import Decimal
from pprint import pprint
import json
import boto3


def update_book(isbn, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url="http://localhost:8000",
            region_name='dummy',
            aws_access_key_id='dummy',
            aws_secret_access_key='dummy')

    table = dynamodb.Table('Books')

    response = table.update_item(
        Key={
            'isbn': int(isbn)
        },
        UpdateExpression="remove rating",
        ReturnValues="UPDATED_NEW"
    )
    return response


if __name__ == '__main__':
    update_response = update_book(9784003202524)
    print("Update book succeeded:")
    pprint(update_response)
