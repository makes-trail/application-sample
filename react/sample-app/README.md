# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## 環境構築

Node.jsとnpmをインストールする。

1. https://nodejs.org/ja/ からLTSがついているバージョンをダウンロード&インストール
2. インストールされたか確認

```
$ node -v
$ npm -v
```

## 必要なパッケージをインストール

npmを使用してパッケージを`/node_modules`配下にインストールする。

```
cd react
cd sample-app
npm install
```

## JSON ServerでAPIモックを作成

[JSON Server](https://github.com/typicode/json-server)を用いて、デモ用のAPIモックサーバをローカルに立てる。

```
npx json-server --watch ./mock/db.json --port 3333
```

ブラウザから http://localhost:3333/fetch-isbn-summary?isbn=9784905325055 にアクセスして、JSONを取得できることを確認。

## Reactアプリを起動

JSON Serverで立てたAPIモックはそのままの状態で、Reactアプリを起動する。（ローカル開発モード）
```
npm run start:dev
```

http://localhost:3000 が自動で開く。

## 環境変数

アプリ起動時に埋め込む環境変数を`.env.development`(ローカル開発用)と`.env`(AWS開発環境用)で定義している。

### `npm run start:dev`

ローカル開発モードでアプリを起動する。

### `npm run start`

AWS開発環境用モードでアプリを起動する。

### `npm run build`

AWS開発環境用のアプリを`/build`配下にビルドする。\
このコマンドで`/build`配下に生成されたファイルたちをS3にアップロードして静的ホスティングする。


## Available Scripts

In the project directory, you can run:

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).
