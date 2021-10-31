# LINEログインを用いた認証機能

## 認証〜ユーザ情報取得の流れ

1. ブラウザから`xxxxxx.cloudfront.net`にアクセス

2. オリジンのS3にルーティング

3. サービス画面から`Log in with LINE`ボタンをクリック

4. Cognitoが提供するHosted UIページに遷移

5. Hosted UIページの`LINE`ボタンをクリック（サードパーティー経由のサインイン：フェデレーション）

6. LINEの認証エンドポイントにリクエスト

7. ユーザとLINEプラットフォーム間でユーザ認証

8. 認証プロセス完了後、CognitoのコールバックURLにリダイレクト

9. Cognitoがよしなに連携して認可コードを発行

10. Amplify（のCognito SDK）がよしなに連携してIDトークン（JWT）を取得

11. IDトークンをAuthorizationヘッダーに埋め込んで、`xxxxxx.cloudfront.net/api/userinfo`にリクエスト

12. オリジンのAPI Gatewayにルーティング

13. API Gatewayの`/userinfo`エンドポイントに設定されたCognitoオーソライザーがトークンを検証

14. Lambda関数が入力（の`requestContext`）からユーザ情報を取得し返却

## アーキテクチャ

![LINE Login Architecture](./image/line-login.drawio.png)
