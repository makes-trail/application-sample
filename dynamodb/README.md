# DynamoDB Local導入およびCRUD操作

## Docker

コンテナ起動（イメージ作成を含む）

```sh
docker-compose up -d --build
```

コンテナ停止

```sh
docker-compose down --remove-orphans
```

コンテナ&イメージ削除

```sh
docker-compose down --rmi local --remove-orphans

# 名前付きボリュームも削除する場合は
docker-compose down --rmi local --volumes --remove-orphans
```
