# AWS CLI設定マニュアル

## コンソール上で設定するもの

### 多要素認証（MFA）

1. AWS マネジメントコンソール上部の`ユーザ名@アカウントID`をクリックし、プルダウンから「マイセキュリティ資格情報」を選択

<img width=1000 src="./image/management_console_top.png">

2. [AWS公式ドキュメント](https://docs.aws.amazon.com/ja_jp/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html?icmpid=docs_iam_console#enable-virt-mfa-for-own-iam-user)などを参考にしてMFAを有効化（下図はすでに有効化が完了しているもの）

<img width=1000 src="./image/iam_mfa.png">

3. 有効化が完了したら一度サインアウトし、再度サインイン（その際MFA認証が要求されればOK）

### アクセスキー

1. AWS マネジメントコンソール上部の`ユーザ名@アカウントID`をクリックし、プルダウンから「マイセキュリティ資格情報」を選択（MFA有効化と同じ画面）

<img width=1000 src="./image/management_console_top.png">

2. 「アクセスキーの作成」をクリック

<img width=1000 src="./image/iam_accesskey.png">

3. ウィンドウが出てくるので、「csvファイルのダウンロード」をクリック（作成したアクセスキーをダウンロードできるのはこの１回限りなので注意）

<img width=1000 src="./image/iam_download_accesskey.png">

4. ダウンロードしたcsvファイルを無くさないように、そして流出しない(!!!)ように、ローカルPC内で大切に保管

> アクセスキーは流出しないように、特に間違えてもGitHubに上げないようにくれぐれも取り扱いには気をつけてください！\
> 流出したらどんなことが起きるのかは下のサイトなどが詳しいです。
> - [GitHub に AWS キーペアを上げると抜かれるってほんと？？？試してみよー！](https://qiita.com/saitotak/items/813ac6c2057ac64d5fef)
