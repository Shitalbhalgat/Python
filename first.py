
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/<name>')
def hello(name):
    return "i am good"+name

if __name__ == '__main__':
    app.run(debug=True)