# Azure
Azureに関するメモ

# サービスプリンシパル

[参考](https://www.slideshare.net/ToruMakabe/3azure-service-principal)

Azureのリソースにアクセスする、アプリケーションやスクリプトの為のID。

ユーザーID情報でアプリケーションやスクリプトを作成すると
ユーザーが異動など行われた時にその対象のアプリケーションやスクリプトが認証エラーになる。

- 認証方式はパスワードor証明書のどちらかを選択。

# Azure cli
- [リファレンス](https://docs.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest)
### ログイン方法
```bash
# azure cli でサインイン
az login
# 以下のようなメッセージが表示され、各自のブラウザで表示されているアドレスにアクセスし、コードを入力する
To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code G4CNX7SWY to authenticate.
```

### リソースグループ
[参考](https://docs.microsoft.com/ja-jp/azure/azure-resource-manager/management/manage-resource-groups-cli)

以下のようなコマンドが存在する。

``` az group <コマンド> <オプション> ```

| コマンド | 概要 |
| -- | -- |
| create | リソースグループを作成 |
| delete | リソースグループを削除 |
| list | json形式のリストでリソースグループ一覧を取得 `--out`で出力形式を指定 (例：az group list --out table) |
| show |```--name```オプションで指定した名前のリソースグループ名の |

### コンテナの作成
[参考](https://docs.microsoft.com/ja-jp/azure/container-instances/container-instances-quickstart)

```bash
 az container create --resource-group <グループ名> --name <コンテナ名> --image <Dockerイメージ名> --dns-name-label <ラベル名> --ports <ポート番号>
```

例：
```
az container create --resource-group sample-group --name samplecontainer --image mcr.microsoft.com/azuredocs/aci-helloworld --dns-name-label acidemo --ports 80
```

作成後、 ``` az container show ```でデプロイの完了したことを受信する事ができる。

```bash
az container show --resource-group sample-group --name samplecontainer --query "{FQDN:ipAddress.fqdn,ProvisioningState:provisioningState}" --out table
```

## コンテナの削除

```
az container delete --resource-group sample-group --name samplegroup
```