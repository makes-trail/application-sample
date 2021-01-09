'''
指定した項目を更新する。

authorとpubdate属性を更新する。
'''

from decimal import Decimal
from datetime import datetime
from pprint import pprint
import json
import boto3


def update_book(isbn, author, pubdate, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url="http://localhost:8000",
            region_name='dummy',
            aws_access_key_id='dummy',
            aws_secret_access_key='dummy')

    table = dynamodb.Table('Books')

    response = table.update_item(
        # 更新する項目のプライマリキーを指定
        Key={
            'isbn': int(isbn)
        },
        UpdateExpression="set author=:a, pubdate=:d",
        # 更新する属性の値を指定
        ExpressionAttributeValues={
            ':a': author,
            ':d': pubdate
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


if __name__ == '__main__':
    today = datetime.now().strftime("%Y-%m-%d")
    update_response = update_book(9784003202524, "魯迅", today)
    print("Update book succeeded:")
    pprint(update_response)
