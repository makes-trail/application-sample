'''
指定した項目を更新する。

rating属性の値を更新する。

[Notes] BooksItemUpdate02.pyを先に実行してrating属性を追加しないとエラーを吐く。
'''

from decimal import Decimal
from pprint import pprint
import json
import boto3


def update_book(isbn, rating_increase, dynamodb=None):
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
        UpdateExpression="set rating = rating + :r",
        ExpressionAttributeValues={
            ':r': int(rating_increase)
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


if __name__ == '__main__':
    # ratingの値を-1する。
    update_response = update_book(9784003202524, -1)
    print("Update book succeeded:")
    pprint(update_response)
