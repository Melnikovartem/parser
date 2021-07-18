from flask import Blueprint, render_template, redirect, url_for, request
from .models import Stock
from . import db

info_stock_app = Blueprint('info_stock_app', __name__)


@info_stock_app.route('/info_stock/<id_stock>')
def info_stock_get(id_stock):
    stock = Stock.query.filter_by(id=id_stock).first()

    return render_template(
        'stock.html',
        data=stock.__to_dict__(),
        comments=stock.get_comments())
