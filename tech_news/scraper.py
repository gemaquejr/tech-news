# Requisito 1
def fetch(url):
    import requests
    import time

    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        return None

    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    import parsel

    selector = parsel.Selector(html_content)
    return selector.css("h2 a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    import parsel

    selector = parsel.Selector(html_content)
# Passou com a ajuda da Maria Carolina na Mentoria
    return selector.css("a.next.page-numbers::attr(href)").get()


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
