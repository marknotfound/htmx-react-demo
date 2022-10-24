from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/button')
def button():
    return render_template("button.html")

@app.route('/some_list')
def some_list():
    return render_template("some_list.html")