# DynamoDB Local導入およびCRUD操作

## Docker

### コンテナ起動（イメージ作成を含む）

```sh
docker-compose up -d --build
```

<details><summary>このようになれば成功</summary><div>

```sh
$ docker-compose ps

          Name                         Command               State           Ports         
-------------------------------------------------------------------------------------------
dynamodb_dynamodb-admin_1   node bin/dynamodb-admin.js       Up      0.0.0.0:8001->8001/tcp
dynamodb_dynamodb_1         java -jar DynamoDBLocal.ja ...   Up      0.0.0.0:8000->8000/tcp
```
</div></details>

http://localhost:8001 にアクセスしてGUIツールが表示されることを確認

### コンテナ停止

```sh
docker-compose down --remove-orphans
```

### コンテナ&イメージ削除

```sh
docker-compose down --rmi local --remove-orphans

# 名前付きボリュームも削除する場合は
docker-compose down --rmi local --volumes --remove-orphans
```

## CRUD操作
> 実行にはPython(バージョン 3.x)環境が必要

- [`boto3`](https://aws.amazon.com/jp/sdk-for-python/)というライブラリを使うので、pipかcondaでインストールする必要がある

```sh
pip install boto3

# Anaconda, Minicondaユーザは
conda install boto3
```

### テーブル作成
```sh
cd crud
python BooksCreateTable.py
```

### データ挿入（Create）
```sh
python BooksItemCreate.py
```

### データ読取（Read）
```sh
python BooksItemRead.py
```

### データ更新（Update）
```sh
# 一部の属性を更新
python BooksItemUpdate01.py

# 新たに属性を追加
python BooksItemUpdate02.py

# 属性値をインクリメント
python BooksItemUpdate03.py

# 属性を削除
python BooksItemUpdate04.py
```

### データ削除（Delete）
```sh
# BooksItemUpdate02.py, BooksItemUpdate03.py を実行してから
python BooksItemDelete.py
```

> 参考記事
> - https://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html
> - https://dev.classmethod.jp/articles/dynamodb-update-expression-actions/
