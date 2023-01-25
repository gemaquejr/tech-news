from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    # https://stackoverflow.com/questions/26699885/how-can-i-use-a-regex-variable-in-a-query-for-mongodb
    query = {"title": {"$regex": title, "$options": "i"}}
    page = search_news(query)
    return [(new["title"], new["url"]) for new in page]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
