'''
指定した項目を条件付きで削除する。

rating属性の値が3以下ならば、その項目を削除する。
'''

from decimal import Decimal
from pprint import pprint
import json
import boto3
from botocore.exceptions import ClientError


def delete_underrated_book(isbn, rating, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url="http://localhost:8000",
            region_name='dummy',
            aws_access_key_id='dummy',
            aws_secret_access_key='dummy')

    table = dynamodb.Table('Books')

    try:
        response = table.delete_item(
            Key={
                'isbn': int(isbn)
            },
            # 削除される条件
            ConditionExpression="rating <= :val",
            ExpressionAttributeValues={
                ":val": int(rating)
            }
        )
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(e.response['Error']['Message'])
        else:
            raise
    else:
        return response


if __name__ == '__main__':
    print("Attempting a conditional delete...")
    delete_response = delete_underrated_book(9784003202524, 3)
    if delete_response:
        print("Delete book succeeded:")
        pprint(delete_response)
