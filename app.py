from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, Canada!</h1>'

@app.route('/hello/<name>/')
def hello(name):
    return render_template(index.html, name=name)
