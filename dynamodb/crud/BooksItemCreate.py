'''
テーブルに項目（item: RDBでいうところのレコード）を挿入する。

１つの項目はプライマリキーと複数の属性（attributes）で構成される。
RDBとは違って、属性のスキーマは項目ごとに異なっていてよい。（各項目ごとに属性のスキーマが定義される。）

PutItemは、べき等の操作である。（何回実行しても得られる結果が同じになる。）
RDBでいうところのINSERTとは違い、同じプライマリキーをもつ項目がすでにテーブルに存在したとしても上書きされる。
'''

from decimal import Decimal
from pprint import pprint
import json
import boto3


def put_book(book, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url="http://localhost:8000",
            region_name='dummy',
            aws_access_key_id='dummy',
            aws_secret_access_key='dummy')

    table = dynamodb.Table('Books')
    response = table.put_item(Item=book)
    return response


# 取得したjsonデータから項目を挿入するための構造に整形
def format_openbd(openbd_json):
    assert len(openbd_json) == 1, "該当の書籍データがありません"

    output_dict = openbd_json[0]["summary"]
    output_dict["isbn"] = int(output_dict["isbn"])  # isbnのデータ型（Number）に合わせるためにキャスト
    return output_dict


if __name__ == '__main__':
    with open("openbd_sample.json", "r") as json_file:
        openbd_json = json.load(json_file, parse_float=Decimal)

    book = format_openbd(openbd_json)
    response = put_book(book)
    print("Put book succeeded:")
    pprint(response)
