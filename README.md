# LINE-Chatbot-Flask-test
LINEチャットボットを試してみた（オウム返しするだけ）

HerokuにデプロイしたあとにLINEの管理画面で「接続確認」してもエラーになるが、LINEで試すと無事に処理される。

@app.route()同士は2行あける（？）VSCodeの問題かもしれないけども。

MacでやるとPython2系がやっかいだった。

参考：
Python初心者がたったの3日間でチャットボットを作った【0日目】
https://yukituna.com/1192/

PythonでLine botを作ってみた
https://qiita.com/krocks96/items/67f7510b36945eb9689b

FlaskでLINE botを実装し，herokuにdeployするまで
https://qiita.com/suigin/items/0deb9451f45e351acf92


おうむ返しだけのはずが、ボタンテンプレート+URIアクションまで試した。
