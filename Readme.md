## streamplayer.html  
本家配信とJapaneseRestreamのチャットが同時に見られるお手軽版プレイヤー  
### 必要環境  
大体のウェブブラウザ（IE非対応、広告ブロッカーが入っているとやや挙動が怪しい）  
### 使い方  
下のURLをクリック  
https://fusowasedr09.github.io/for-Japanese_Restream/streamplayer.html  
  
## roleset.py  
Japanese RestreamのDiscordのイベント毎カテゴリ（〇〇解説、〇〇スタッフ）の設定が（だいたい）できるDiscordのbot。専用機なのでbotのビルドが必要。  
### 必要環境
・Python 3.8~
・discord.py 1.7~
・botのアカウント
### 使い方  
1.botに「manage Roles」「Manage channels」「View Channel」「Send message」の権限を渡して招待  
2.botを起動させる  
3.botが読めるチャンネルで「/create_(イベント名)」と発言する(アンダースコアは半角スペースに置き換え)
4.あとは勝手に（イベント名）スタッフ、（イベント名）解説がついたプライベートチャンネルを作ってくれます  
（ただし、スレッド関係など一部権限に対応しない他、事故防止のために既存チャンネルを触らないように設定しているため、その辺りは注意）
5.botを終了する
###　注意点
既存チャンネルは一切触らないのでその兼ね合いが必要なら個別設定をお願いします。  
名称が間違ってもチェックしないので起動コマンド入れる時には要注意。  
また、複数作成もチェックしていないため気をつけること。  
間違った場合、削除機能は入っていないためAdministratorに削除してもらってください。
