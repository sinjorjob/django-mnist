# django-deap-learning-mnist-sample

ディープラーニング＋DjangoでMNIST(手書き数字画像認識)を実際に動かして試せるサンプルアプリです。

解説：（sinyのURL: https://sinyblog.com/django/ai_api_001/）

# 使い方

１．事前にpython(3.6以上)をインストールする。

２．gitでプロジェクトをダウンロードする

```
git clone https://github.com/sinjorjob/mnist_tutorial.git
```

※右上の「Clone or Download」→ 「Download ZIP」からダウンロードでもOKです。

３．DOS画面よりセットアップコマンドを実行する

windows

```
cd django-mnist-master
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

4. views.pyの10行目の学習モデルファイルパス<path>を環境に合わせて修正する。

```
model = load_model('C:\\<path>\\mnist.h5')
```
5. マイグレーションを実行する。
```
python manage.py migrate
```


MacOS/Linuxでは動作確認していませんが、同様の手順で実装できると思います。

6. 開発サーバを立ち上げてブラウザからURLを開く

windows

```
python manage.py runserver
```


7. 以下のURLにアクセスする。

```
http://localhost:8000/mnist
```

8. 補足

examplesフォルダ：kerasによるモデル定義～学習～モデル保存までのコード一式
modelフォルダ：デモアプリ用の学習済みファイル
sampleフォルダ：手書き数字画像のサンプルファイル