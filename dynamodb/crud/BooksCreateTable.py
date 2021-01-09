'''
テーブルを作成する。

プライマリキーには、以下の２種類がとれる。
1. バーティションキーのみ
2. パーティションキーとソートキーの組み合わせ

今回は1の「パーティションキーのみ」で作成する。
'''

import boto3


def create_book_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url="http://localhost:8000",
            region_name='dummy',
            aws_access_key_id='dummy',
            aws_secret_access_key='dummy')

    table = dynamodb.create_table(
        TableName='Books',
        KeySchema=[
            {
                'AttributeName': 'isbn',
                'KeyType': 'HASH'  # Partition key
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'isbn',
                'AttributeType': 'N'  # 数字（Number）型
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


if __name__ == '__main__':
    book_table = create_book_table()
    print("Table status:", book_table.table_status)
