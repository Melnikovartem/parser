from .models import Stock, Comment
from . import db

def scraping_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    all_comments = soup.find_all("div", {"class": "rev__node-body"})

    data = []

    for comment in all_comments:
        info = {}
        info["text"] = comment.find("div", {"class": "rev__node-text"})
        info["author"] = comment.find("div", {"class": "rev__node-head_author"})
        info["date"] = comment.find("div", {"class": "rev__node-date"})
        data.append(info)

    return data

def update_stock(stock_id):
    stock = db.session.query(Stock).filter_by(id=stock_id).first()

    if stock:
        data = scraping_url(stock.link_lamoda)

        for info in data:
            new_comment = Comment(stock_id = stock.id, text=info['text'], author=info['author'], date=info['date'])

            db.session.add(new_comment)
            db.session.commit()
