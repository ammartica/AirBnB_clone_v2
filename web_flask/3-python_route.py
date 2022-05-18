#!/usr/bin/python3
"""Script that starts a Flask web app and displays certain messages"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<string:name>')
def cname(name=None):
    name = name.replace("_", " ")
    return "C {}".format(name)


@app.route('/python/', defaults={'text': "is cool"})
@app.route('/python/<string:text>')
def pythontext(text="is cool"):
    text = text.replace("_", " ")
    return "Python {}".format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
