# AWS CLI設定マニュアル

## コンソール上で設定するもの

### 多要素認証（MFA）

#### 1. AWS マネジメントコンソール上部の`ユーザ名@アカウントID`をクリックし、プルダウンから「マイセキュリティ資格情報」を選択

<details><summary>画像を見る</summary><div>
<img width=1000 src="./image/management_console_top.png">
</div></details>

#### 2. [AWS公式ドキュメント](https://docs.aws.amazon.com/ja_jp/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html?icmpid=docs_iam_console#enable-virt-mfa-for-own-iam-user)などを参考にしてMFAを有効化

下図はすでに有効化が完了しているものです。

<details><summary>画像を見る</summary><div>
<img width=1000 src="./image/iam_mfa.png">
</div></details>

#### 3. 有効化が完了したら一度サインアウトし、再度サインイン

その際MFA認証が要求されればOKです。

### アクセスキー

#### 1. AWS マネジメントコンソール上部の`ユーザ名@アカウントID`をクリックし、プルダウンから「マイセキュリティ資格情報」を選択

MFA有効化と同じ画面です。

<details><summary>画像を見る</summary><div>
<img width=1000 src="./image/management_console_top.png">
</div></details>

#### 2. 「アクセスキーの作成」をクリック

<details><summary>画像を見る</summary><div>
<img width=1000 src="./image/iam_accesskey.png">
</div></details>

#### 3. ウィンドウが出てくるので、「csvファイルのダウンロード」をクリック

作成したアクセスキーをダウンロードできるのはこの１回限りなので注意してください。

<details><summary>画像を見る</summary><div>
<img width=1000 src="./image/iam_download_accesskey.png">
</div></details>

#### 4. ダウンロードしたcsvファイルを無くさないように、そして流出しない(!!!)ように、ローカルPC内で大切に保管

> アクセスキーは流出しないように、特に間違えてもGitHubに上げないようにくれぐれも取り扱いには気をつけてください！\
> 流出したらどんなことが起きるのかは下のサイトなどが詳しいです。
> - [GitHub に AWS キーペアを上げると抜かれるってほんと？？？試してみよー！](https://qiita.com/saitotak/items/813ac6c2057ac64d5fef)

### スイッチロール

開発チームのIAMユーザーにアタッチされているIAMポリシーは`PowerUserAccess`です。なのでIAMまわりの参照・変更は総じてできないようになっています。\
ですがLambdaの実行ロールを作成・編集するためにはIAMロールやIAMポリシーを参照・変更する必要が出てきます。\
そこで`ApplicationDeveloperRole`というIAMロールを用意しています。そこには`PowerUserAccess`以外にLambdaの実行ロールを作成・編集するためのポリシーがアタッチされています。\
開発チームのIAMユーザーはこのIAMロールにスイッチすることでLambdaまわりの設定を行えるようになります。

#### 1. AWS マネジメントコンソール上部の`ユーザ名@アカウントID`をクリックし、プルダウンから「ロールの切り替え」を選択

<details><summary>画像を見る</summary><div>
<img width=1000 src="./image/management_console_switch_role.png">
</div></details>

#### 2. 以下の項目を入力して「ロールの切り替え」をクリック

- アカウント: `25*********4`（「マイアカウント」の横に表示されているもの）
- ロール: `ApplicationDeveloperRole`
- 表示名: `{名前}-app`（任意ですがこうしておくと分かりやすいと思います）
- 色: 自由に好きな色を選んでください

<details><summary>画像を見る</summary><div>
<img width=1000 src="./image/iam_switch_role.png">
</div></details>

#### 3. 切り替え後の画面

下図のようになったらOKです。

<details><summary>画像を見る</summary><div>
<img width=1000 src="./image/iam_switch_role_done.png">
</div></details>

