# Azure cli

Azure cliを行う為の環境

# How to Run

```bash
# az フォルダ階層に移動する。
cd az
# コンテナを起動しログインする
docker-compose up -d
docker-compose exec az /bin/bash

# もしくは
docker-compose run az ...
```