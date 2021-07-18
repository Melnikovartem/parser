from flask import Flask, render_template, request, redirect, url_for, Blueprint
from .models import Stock, Comment

main_app = Blueprint('main_app', __name__)

@main_app.route('/', methods = ["GET"])
def main():
    stocks_data = []
    return render_template("index.html", stocks_data = stocks_data)

@main_app.route('/info', methods = ["GET"])
def info():
    return render_template("info.html")
