from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!要ttf'

//我的修改2
if __name__ == '__main__':
    app.run()
