from random import randint

import pytest
from tests.conftest import client


@pytest.mark.asyncio
async def test_get_sneakers():
    response = client.get(
        f"http://0.0.0.0:8002/api/v1/lamoda/?page={randint(1, 10)}"
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


@pytest.mark.asyncio
async def test_get_sneakers_hrefs():
    response = client.get(
        f"http://0.0.0.0:8002/api/v1/lamoda/hrefs/{randint(1, 10)}"
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


@pytest.mark.asyncio
async def test_get_sneaker_by_href():
    response = client.get(
        "http://0.0.0.0:8002/api/v1/lamoda/detail/href/?href=/p/rtladl534401/shoes-napapijri-krossovki/"
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


@pytest.mark.asycnio
async def test_get_sneaker_by_article():
    response = client.get(
        "http://0.0.0.0:8002/api/v1/lamoda/detail/article/?article=rtlada874801"
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
