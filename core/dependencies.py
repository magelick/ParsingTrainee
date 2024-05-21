import requests
from bs4 import BeautifulSoup
from requests import Response


def get_bs4_object(url: Response) -> BeautifulSoup:
    """
    Func which return BeautifulSoup instance
    :param url:
    :return:
    """
    return BeautifulSoup(url.text, "lxml")


def get_url(url: str) -> Response:
    """
    Func which return Response instance
    :param url:
    :return:
    """
    return requests.get(url=url)
