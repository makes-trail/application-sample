from pprint import pprint
import json
import boto3
from botocore.exceptions import ClientError


def get_book(isbn, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url="http://localhost:8000",
            region_name='dummy',
            aws_access_key_id='dummy',
            aws_secret_access_key='dummy')

    table = dynamodb.Table('Books')

    try:
        response = table.get_item(Key={'isbn': isbn})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    sample_isbn = 9784003202524
    book = get_book(sample_isbn)
    if book:
        print("Get book succeeded:")
        pprint(book, sort_dicts=False)
