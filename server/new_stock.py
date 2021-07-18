from flask import Flask, render_template, request, redirect, url_for, Blueprint
from .models import Stock, Comment
from . import db

new_stock_app = Blueprint('new_stock_app', __name__)
atr_req = ['name', 'link']


@new_stock_app.route('/new_stock', methods=['POST'])
def new_stock():
    data = {}
    for form in atr_req:
        if form in request.form:
            data[form] = request.form.get(form)

    if data:
        if list(data.keys()) == atr_req:
            new_stock = Stock(link_lamoda=data['link'], name=data['name'])
            db.session.add(new_stock)
            db.session.commit()

    return redirect('/')
