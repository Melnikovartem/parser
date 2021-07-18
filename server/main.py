from flask import Flask, render_template, request, redirect, url_for, Blueprint
from .models import Stock

main_app = Blueprint('main_app', __name__)

def list_stocks():
    return list(map(lambda x: x.__to_dict__(), Stock.query.all()))

@main_app.route('/', methods = ["GET"])
def main():
    return render_template("index.html", stocks_data = list_stocks())

@main_app.route('/info', methods = ["GET"])
def info():
    return render_template("info.html")
