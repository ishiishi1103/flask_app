# coding: utf-8

from flask import Flask, render_template

# インスタンス化
app = Flask(__name__)

# view側の設定
# ルートディレクトリにアクセスしたときの挙動
@app.route('/')
def index():
   # return 'Hello World'
   return render_template('index.html')

if __name__ == '__main__':
    app.run()