# 環境構築手順

## エディター

- [Visual Studio Code](https://code.visualstudio.com/)のインストール
  - React、Lambdaの開発に使用します。

## ツール/パッケージ

- [git](https://git-scm.com/downloads)のインストール
  - 本リポジトリのコードを取得・更新するために使用します。
  - 改行コードをCRLFに変換しないように、コード取得前に下記のコマンドを実行しておきます。
    ```bash
    git config --global core.autocrlf input
    ```

- [AWS CLI](https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/cli-chap-install.html)のインストール
  - Pythonインストール後に下記コマンドでインストール可能です。
    ```bash
    pip install awscli
    # もしくは
    pip3 install awscli
    ```
  - 下記コマンドで確認
    ```bash
    aws --version
    ```

- [Node.js/npm](https://nodejs.org/ja/download/)のインストール
  - React、Lambdaの開発のために使用します。
  - Node.jsの最新LTS版をインストールしてください。
  - 下記コマンドで確認
    ```bash
    node --version
    npm --version
    ```

- [Docker](https://www.docker.com/)のインストール
  - [Windows用](https://docs.docker.com/docker-for-windows/install/)
  - [Mac用](https://docs.docker.com/docker-for-mac/install/)
  - Lambda関数をパッケージ化するために使用します。

### Windows限定
以下はWindows環境のみ必要なツール/パッケージです。

- [Make for Windows](http://gnuwin32.sourceforge.net/packages/make.htm)のインストール
  - docker-composeコマンドをMakefileで集約しているため、makeコマンドを使用します。

- zipコマンドのインストール
  - Windowsには標準でzipコマンドが備わっていない。
