# discord-remo-bot

NatureRemoの室温をDiscordに通知するbotのソースコードです．

※ 利用にはDiscordのBot及びチャンネルの作成及びチャンネルID・トークンの取得が必要です: [参考) Botの作り方について](https://discordpy.readthedocs.io/ja/latest/discord.html)

※ 気温と湿度の通知にはNatureRemoを購入する必要があり，かつNatureRemo APIを使用するためのトークン取得が必要です 参考) [Nature Remoの概要](https://nature.global/), [APIについて](https://developer.nature.global/)

# 実行方法
## 環境
- Python 3.7.6
- discord 1.0.1
- Docker-compose 1.2.1
- Docker 19.03.5
- Raspberry Pi 3 ModelB+ (Raspbian, 64bit)

実行はDocker-composeを推奨しており，```Docker-compose up -d```コマンドだけでBotが起動します．
Docker-composeを使用した場合に限り，"実行しているサーバーのIPアドレス:8080/env"にアクセスすると気温と湿度の推移を確認できます．

## Pythonコマンドを使用する場合
もしdocker-composeが使用できない場合は，以下のコマンドを実行してください(Pythonの仮想環境である[venv](https://www.python.jp/install/windows/venv.html)の利用をお勧めします)
1. python -m venv .env 
1. .env/Scripts/Activate.ps1(WindowsのPowershellの場合) or .env/bin/activate (Linuxの場合)
1. pip install discord pytz
1. python remo_main.py


## Docker-composeを使う場合
1. Docker-composeをインストールする 参考)[Docker-composeについて](https://docs.docker.com/compose/install/)
1. DiscordのAPI用のトークン，Botを使用するDiscordのチャンネルID，NatureRemoのAPI用トークンを取得する
1. remo/config.iniに取得したトークンを追記する
1. ```docker-compose up```で実行

# その他
- 間違いや修正はIssueかTwitter(@10_2rugata)まで
- プルリクエスト大歓迎です

# 履歴
2020/11/04 公開
