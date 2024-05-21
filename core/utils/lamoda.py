from typing import Dict

from core.dependencies import get_url, get_bs4_object


def get_all_sneakers(page_int: int) -> Dict:
    """
    Func which get all sneakers on page
    :param:
    :return:
    """
    # create url and parsing them
    url = f"http://www.lamoda.by/c/5971/shoes-muzhkrossovki/?sitelink=topmenuM&l=4&page={page_int}"
    response = get_url(url=url)
    soup = get_bs4_object(url=response)
    # create response data
    data = {}
    # interation by tag values
    for item in soup.find_all(name="div", class_="x-product-card-description"):
        # get brand value
        brand = (
            item.find(
                name="div", class_="x-product-card-description__brand-name"
            )
            .get_text()
            .strip()
        )
        # get model value
        model = (
            item.find(
                name="div", class_="x-product-card-description__product-name"
            )
            .get_text()
            .strip()
        )
        # get price value
        price = item.find(name="span").get_text().strip()
        # add all values in response data
        data[brand] = {
            "model": model.replace("Кроссовки", "").strip(),
            "price": price,
        }
    # return response data
    return data


def get_sneakers_hrefs(page_int: int) -> Dict:
    """
    Func which get all sneakers hrefs on page
    :param page_int:
    :return:
    """
    # create url and parsing them
    url = f"https://www.lamoda.by/c/5971/shoes-muzhkrossovki/?sitelink=topmenuM&l=4&page={page_int}"
    response = get_url(url=url)
    soup = get_bs4_object(url=response)
    # create response data
    data = {}
    # interation by tag values
    for item in soup.find_all(name="div", class_="x-product-card__card"):
        # get brand value
        brand = (
            item.find(
                name="div", class_="x-product-card-description__brand-name"
            )
            .get_text()
            .strip()
        )
        # get model value
        model = (
            item.find(
                name="div", class_="x-product-card-description__product-name"
            )
            .get_text()
            .strip()
        )
        # get href value
        href = item.find(
            "a", class_="x-product-card__link x-product-card__hit-area"
        ).get("href")
        # add all values in response data
        data[f"{brand}{model.replace('Кроссовки', '')}"] = href
    # return response data
    return data


def get_sneaker_by_href(href: str) -> Dict:
    """
    Func which get sneaker by href
    :param href:
    :return:
    """
    # create url and parsing them
    url = f"https://www.lamoda.by/{href}"
    response = get_url(url=url)
    soup = get_bs4_object(url=response)
    # get lists which includes title and attribute values
    titles = [
        "".join(title.get_text().strip().replace(" .", ""))
        for title in soup.find_all(
            "span", class_="x-premium-product-description-attribute__title"
        )
    ]
    values = [
        "".join(value.get_text().strip().replace(" .", ""))
        for value in soup.find_all(
            "span", class_="x-premium-product-description-attribute__value"
        )
    ]
    # create response data
    data = {}
    # add all titles with values in response data
    for title, value in zip(titles, values):
        data[title] = value
    # interation by tag values
    for item in soup.find_all("main", class_="width-wrapper"):
        # get brand value
        data["Бренд"] = (
            item.find("span", class_="x-premium-product-title__brand-name")
            .get_text()
            .strip()
        )
        # get model value
        data["Модель"] = (
            item.find("div", class_="x-premium-product-title__model-name")
            .get_text()
            .strip()
            .replace("Кроссовки", "")
        )
        # get price value
        data["Цена"] = (
            item.find("span", class_="x-premium-product-prices__price")
            .get_text()
            .strip()
        )
    # return response data
    return data


def get_sneaker_by_article(article: str) -> Dict:
    """
    Func witch get sneaker by article
    :param article:
    :return:
    """
    # create url and parsing them
    url = f"https://www.lamoda.by/p/{article}"
    response = get_url(url=url)
    soup = get_bs4_object(url=response)
    # get lists which includes title and attribute values
    titles = [
        "".join(title.get_text().strip().replace(" .", ""))
        for title in soup.find_all(
            "span", class_="x-premium-product-description-attribute__title"
        )
    ]
    values = [
        "".join(value.get_text().strip().replace(" .", ""))
        for value in soup.find_all(
            "span", class_="x-premium-product-description-attribute__value"
        )
    ]
    # create response data
    data = {}
    # add all titles with values in response data
    for title, value in zip(titles, values):
        data[title] = value
    # interation by tag values
    for item in soup.find_all("main", class_="width-wrapper"):
        data["Бренд"] = (
            item.find("span", class_="x-premium-product-title__brand-name")
            .get_text()
            .strip()
        )
        data["Модель"] = (
            item.find("div", class_="x-premium-product-title__model-name")
            .get_text()
            .strip()
            .replace("Кроссовки", "")
        )
        data["Цена"] = (
            item.find("span", class_="x-premium-product-prices__price")
            .get_text()
            .strip()
        )
    # return response data
    return data
