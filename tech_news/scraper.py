from tech_news.database import create_news


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
    import parsel

    selector = parsel.Selector(html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("a.url.fn.n::text").get()
    comments_count = selector.css("div.comment-body").getall()
    # Referência: https://developer.mozilla.org/en-US/docs/Web/CSS/:nth-of-type
    summary = selector.css(
        ".entry-content > p:nth-of-type(1) *::text"
    ).getall()
    tags = selector.css(".post-tags a::text").getall()
    category = selector.css("span.label::text").get()

    return {
        "url": url,
        "title": (title).strip(),
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": int(comments_count) if comments_count else 0,
        "summary": "".join(summary).strip(),
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    URL_BASE = "https://blog.betrybe.com"
    list_urls = []

    # Refer.: https://www.w3schools.com/python/python_lists_comprehension.asp
    def get_link_page(links):
        new_list = [scrape_news(fetch(url)) for url in links[:(amount)]]
        return new_list

    def get_urls(url):
        list_urls.extend(scrape_updates(fetch(url)))

        if len(list_urls) <= amount:
            next_url = scrape_next_page_link(fetch(url))
            get_urls(next_url)

        return get_link_page(list_urls)

    final_result = get_urls(URL_BASE)
    create_news(final_result)
    return final_result
