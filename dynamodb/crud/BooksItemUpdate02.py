'''
指定した項目を更新する。

ratingという属性を新たに追加して、そこに値を代入する。
'''

from decimal import Decimal
from pprint import pprint
import json
import boto3


def update_book(isbn, rating, dynamodb=None):
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
        UpdateExpression="set rating=:r",
        ExpressionAttributeValues={
            ':r': int(rating)
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


if __name__ == '__main__':
    update_response = update_book(9784003202524, 4)
    print("Update book succeeded:")
    pprint(update_response)
