from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, it is my syte)'


@app.route('/about')
def about_blank():
    return 'it is about blank '


if __name__ == '__main__':
    app.run(debug=True)
