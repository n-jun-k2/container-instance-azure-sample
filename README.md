# container-instance-azure-sample
Azure container instance sample

# Documnet list
- [ファイヤーウォールについて](/doc/fire_wall.md)
- [パブリックIP、プライベートIPについて](/doc/public_ip.md)
- [wsl環境での開発について](/doc/wsl_env.md)
- [azure_cliについて](/doc/azure_cli.md)

# How to run
dockerをgithub container restry(ghcr.io)にログイン
```bash
# トークン番号を記録されているファイルを作成
echo <token number> > ghcr.txt
# ghcr.ioにログイン(windowsはcat=type)
cat ghcr.txt | docker login ghcr.io -u <githubユーザ名> --password-stdin
```
envファイルを作成する
```bash
# IPv4のアドレスを記載する
echo LOCAL_ADDRESS=<192.168...> > .env
```
作成後
```bash
# イメージの取得
docker pull ghcr.io/n-jun-k2/container-instance-azure-sample/flask_python:v1
# サービスに必要なコンテナを全て立ち上げる。
docker-compose up -d
# pythonの開発環境にログイン
docker-compose exec python /bin/bash
```

# Connect to the server
```
http://localhost:5000/....
```
