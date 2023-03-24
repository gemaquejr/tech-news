# Requisito 12
import sys
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
)
from tech_news.scraper import get_tech_news


def option_0():
    num_news = input("Digite quantas notícias serão buscadas:")
    return get_tech_news(int(num_news))


def option_1():
    title = input("Digite o título:")
    return search_by_title(title)


def option_2():
    date = input("Digite a data no formato aaaa-mm-dd:")
    return search_by_date(date)


def option_3():
    tag = input("Digite a tag:")
    return search_by_tag(tag)


def option_4():
    category = input("Digite a categoria:")
    return search_by_category(category)


def option_5():
    return top_5_news()


def option_6():
    return top_5_categories()


def option_7():
    return print("Encerrando script\n")


def analyzer_menu():
    """Seu código deve vir aqui"""
    option = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n"
    )

    menu_options = {
        "0": option_0,
        "1": option_1,
        "2": option_2,
        "3": option_3,
        "4": option_4,
        "5": option_5,
        "6": option_6,
        "7": option_7,
    }

    try:
        return menu_options[option]()
    except KeyError:
        print("Opção inválida", file=sys.stderr)
