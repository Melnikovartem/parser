from . import db
from json import dumps

marketplaces = {0: "lamoda"} # todo завести табличку для маркетплейсов и сделать в комментах внешних ключом
# мб можно ссылки тоже хранить в отдельной модели с внешним ключом. По хорошему это более правильная идя архитекуры?

# наш товар, для которого будем добавлять ссылки на маркетплейсы
class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(100))
    link_lamoda = db.Column(db.String(100))

    def __init__(self, **kwargs):
        super(Stock, self).__init__(**kwargs)

# храним текст коммента и к какому товру он принадлежит
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    stock_id = db.Column(db.Integer, unique=True)
    text = db.Column(db.String(1000))
    stars = db.Column(db.Integer, default=0)
    type = db.Column(db.Integer, default=0)
    date = db.Column(db.String(100))
    author = db.Column(db.String(100))
    new = db.Column(db.Boolean, default=1)

    def __init__(self, **kwargs):
        super(Comment, self).__init__(**kwargs)

    def count_new_comments(self, stock_id):
        num = db.session.query(Comment).filter_by(stock_id=stock_id, new=1).count()
        return num
