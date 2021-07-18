import requests
from bs4 import BeautifulSoup

def scraping_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
    except:
        return []
    all_comments = soup.find_all("div", {"class": "rev__node-body"})

    data = []

    for comment in all_comments:
        info = {}
        info["text"] = comment.find("div", {"class": "rev__node-text"}).text
        info["author"] = comment.find("span", {"class": "rev__node-head_author"}).text
        info["date"] = comment.find("span", {"class": "rev__node-date"}).text
        data.append(info)
        print(info)
    return data
