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

npmを使用して依存パッケージを`node_modules`配下にインストールする。

```
cd amplify-app
npm install
```

## 環境変数

アプリ起動時に埋め込む環境変数を`.env`で定義している。
> `.env`はGit管理に上がらない。ローカルにのみ持っておき、公開しないようにする。
> ```bash
> # .env
> REACT_APP_API_ENDPOINT=__API Gatewayでデプロイされているエンドポイント__
> ```

Amplifyライブラリが読み込むCognitoユーザープールの設定を`src/amplifyConfig.ts`で定義している。

`amplifyConfig.sample.ts`を参考に`amplifyConfig.ts`を以下の要領で書き換える。

```ts
const COGNITO_REGION = 'us-west-2';
const COGNITO_USER_POOL = 'us-west-2_xxxxxx'; // プールID
const COGNITO_USER_POOL_CLIENT = 'xxxxxx'; // アプリクライアントID
const COGNITO_DOMAIN_PREFIX = 'xxxxxx'; // ドメインのプレフィックス

const amplifyConfig = {
  Auth: {
    region: COGNITO_REGION,
    userPoolId: COGNITO_USER_POOL,
    userPoolWebClientId: COGNITO_USER_POOL_CLIENT,
    oauth: {
      domain: `${COGNITO_DOMAIN_PREFIX}.auth.${COGNITO_REGION}.amazoncognito.com`,
      scope: [
        'openid',
        'profile'
      ],
      redirectSignIn: 'https://xxxxxx.cloudfront.net', // アプリクライアントのコールバックURL
      redirectSignOut: 'https://xxxxxx.cloudfront.net', // アプリクライアントのサインアウトURL
      responseType: 'code'
    }
  }
};

export default amplifyConfig;
```

## Reactアプリの起動とビルド

### `npm run start`

アプリをローカルホストで起動する。（`.env`の環境変数が読まれる）

### `npm run build`

アプリを`build`配下にビルドする。（`.env`の環境変数が読まれる）\
このコマンドで`build`配下に生成されたファイルたちをS3にアップロードして静的ホスティングする。
