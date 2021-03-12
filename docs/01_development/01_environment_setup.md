# 環境構築手順

## エディター

- [Visual Studio Code](https://code.visualstudio.com/)のインストール
  - React、Lambdaの開発に使用します。

## ツール/パッケージ

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
  - Lambda関数をパッケージ化するためなどに使用します。
  - WindowsとMacでインストール手順が異なります。以下リンクにあるマニュアルにしたがってインストールしてください。
    - [Install Docker Desktop on Windows](https://docs.docker.com/docker-for-windows/install/)
    - [Install Docker Desktop on Mac](https://docs.docker.com/docker-for-mac/install/)

### Windows限定
以下はWindows環境でのみ必要となる設定です。\
macOSの場合は`xcode-select --install`を実行すれば以下の各ツールが標準でインストールされます。

- [Git](https://git-scm.com/downloads)のインストール
  - 本リポジトリのコードを取得・更新するために使用します。
  - 改行コードをCRLFに変換しないように、コード取得前に下記のコマンドを実行しておきます。
    ```bash
    git config --global core.autocrlf input
    ```

- [make](http://gnuwin32.sourceforge.net/packages/make.htm)コマンドのインストール
  - docker-composeコマンドをMakefileで集約しているため、makeコマンドを使用します。
  - 実際のインストール手順は[こちらの記事](https://qiita.com/taki-ikat/items/f501f44a8d44e3fd6987)を参照してください。

- [zip](http://gnuwin32.sourceforge.net/packages/zip.htm)コマンドのインストール
  - Windowsには標準でzipコマンドが備わっていません。
  - makeコマンドと同じ要領で`Complete package, except sources`の<u>`Setup`</u>からダウンロードしてきたインストーラ（exeファイル）を起動してインストールしてください。
