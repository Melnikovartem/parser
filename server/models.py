from . import db
from json import dumps
from .scrapper import scraping_url

# todo завести табличку для маркетплейсов и сделать в комментах внешних ключом
marketplaces = {0: "lamoda"}
# мб можно ссылки тоже хранить в отдельной модели с внешним ключом. По
# хорошему это более правильная идя архитекуры?

# наш товар, для которого будем добавлять ссылки на маркетплейсы


class Stock(db.Model):
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    link_lamoda = db.Column(db.String(100))

    def __init__(self, **kwargs):
        super(Stock, self).__init__(**kwargs)

    def __to_dict__(self):
        self.update_comments()
        data = {}
        data['id'] = self.id
        data['name'] = self.name
        data['links'] = {'lamoda': self.link_lamoda}
        data['new_messages'] = Comment.query.filter_by(
            stock_id=self.id, new=1).count()
        return data

    def update_comments(self):
        data = scraping_url(self.link_lamoda)

        for info in data:
            old_comment = Comment.query.filter_by(text=info['text']).first()
            if not old_comment:
                new_comment = Comment(
                    stock_id=self.id,
                    text=info['text'],
                    author=info['author'],
                    date=info['date'])

                db.session.add(new_comment)
                db.session.commit()

    def get_comments(self):
        return list(map(lambda x: x.__to_dict__(),
                        Comment.query.filter_by(stock_id=self.id).all()))

# храним текст коммента и к какому товру он принадлежит


class Comment(db.Model):
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    stock_id = db.Column(db.Integer)
    text = db.Column(db.String(1000))
    stars = db.Column(db.Integer, default=0)
    type = db.Column(db.Integer, default=0)
    date = db.Column(db.String(100))
    author = db.Column(db.String(100))
    new = db.Column(db.Boolean, default=1)

    def __init__(self, **kwargs):
        super(Comment, self).__init__(**kwargs)

    def __to_dict__(self):
        data = {}
        data['stock_id'] = self.stock_id
        data['text'] = self.text
        data['type'] = self.type
        data['date'] = self.date
        data['author'] = self.author
        return data
