# Requisito 10
from pymongo import MongoClient

client = MongoClient()
db = client.tech_news


def top_5_news():
    """Seu código deve vir aqui"""
    news_list = list(db.news.find().sort("comments_count", -1))
    top_5 = news_list[:5]
    return [(new["title"], new["url"]) for new in top_5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
