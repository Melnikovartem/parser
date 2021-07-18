from flask import Flask, render_template, request, redirect, url_for
import json


app = Flask(__name__)

@app.route('/', methods = ["GET"])
def main():
    stocks_data = []
    return render_template("index.html", stocks_data = stocks_data)

@app.route('/info', methods = ["GET"])
def info():
    return render_template("info.html")


if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)
