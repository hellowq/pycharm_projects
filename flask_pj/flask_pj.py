from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World need chengxuyuan!'


if __name__ == '__main__':
    app.run()
