from random import randint

import pytest

from tests.conftest import client


@pytest.mark.asyncio
async def test_get_sneakers(get_init_cache):
    base_url = "http://0.0.0.0:8002/api/v1/lamoda/"
    page = randint(1, 10)
    url = f"{base_url}?page={page}"

    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_sneakers_hrefs(get_init_cache):
    base_url = "http://0.0.0.0:8002/api/v1/lamoda/hrefs/"
    page = randint(1, 10)
    url = f"{base_url}{page}"

    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_sneaker_by_href(get_init_cache):
    base_url = "http://0.0.0.0:8002/api/v1/lamoda/detail/href/"
    href = "/p/rtladl534401/shoes-napapijri-krossovki/"
    url = f"{base_url}?href={href}"

    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.asycnio
async def test_get_sneaker_by_article(get_init_cache):
    base_url = "http://0.0.0.0:8002/api/v1/lamoda/detail/article/"
    article = "rtlada874801"
    url = f"{base_url}?article={article}"

    response = client.get(url)

    assert response.status_code == 200
