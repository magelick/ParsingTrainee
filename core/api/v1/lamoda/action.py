from typing import List

from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from fastapi_cache.decorator import cache
from pydantic import PositiveInt
from starlette import status

from core.types.lamoda import (
    SneakerParserBasic,
    SneakerParserHrefBasic,
    SneakerDetail,
)


from core.utils.lamoda import (
    get_all_sneakers,
    get_sneakers_hrefs,
    get_sneaker_by_href,
    get_sneaker_by_article,
)

from core.dependencies import check_data_on_exist, add_into_topic

# lamoda router
router = APIRouter(
    prefix="/lamoda",
    default_response_class=ORJSONResponse,
    tags=["Lamoda Actions"],
)


@router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    response_model=List[SneakerParserBasic],
    summary="Get all sneakers on some page",
)
@cache()
async def get_sneakers(page: PositiveInt) -> List[SneakerParserBasic]:
    """
    Endpoint which get all sneakers from page
    :param page:
    :return:
    """
    # get all sneakers on page
    sneakers = get_all_sneakers(page_int=page)
    # validate sneakers data
    data = [
        SneakerParserBasic(brand=brand, info=info)
        for brand, info in sneakers.items()
    ]
    # check validate data on exist
    check_data_on_exist(validate_data=data)  # type: ignore
    # add valid data into topic
    add_into_topic(topic_name="lamoda-list-sneakers-topic", data=sneakers)
    # return valid data
    return data


@router.get(
    path="/hrefs/{href_page}",
    status_code=status.HTTP_200_OK,
    response_model=List[SneakerParserHrefBasic],
    summary="Get all sneaker hrefs on some page",
)
@cache()
async def get_hrefs(
    href_page: PositiveInt,
) -> List[SneakerParserHrefBasic]:
    """
    Endpoint which get sneaker hrefs from page
    :param href_page:
    :return:
    """
    # get all sneaker hrefs on page
    sneaker_hrefs = get_sneakers_hrefs(page_int=href_page)
    # validate hrefs data
    data = [
        SneakerParserHrefBasic(sneaker=sneaker, href=href)
        for sneaker, href in sneaker_hrefs.items()
    ]
    # check validate data on exist
    check_data_on_exist(validate_data=data)  # type: ignore
    # add valid data into topic
    add_into_topic(
        topic_name="lamoda-list-sneaker-hrefs-topic", data=sneaker_hrefs
    )
    # return valid data
    return data


@router.get(
    path="/detail/href/",
    status_code=status.HTTP_200_OK,
    response_model=List[SneakerDetail],
    summary="Get sneaker by href yourself",
)
@cache()
async def get_sneaker_detail_by_href(href: str) -> List[SneakerDetail]:
    """
    Endpoint which get sneaker info by href
    :param href:
    :return:
    """
    # get sneaker detail on page by href
    sneaker = get_sneaker_by_href(href)
    # validate sneaker data
    data = [
        SneakerDetail(title=title, value=value)
        for title, value in sneaker.items()
    ]
    # check validate data on exist
    check_data_on_exist(validate_data=data)  # type: ignore
    # add valid data into topic
    add_into_topic(topic_name="lamoda-sneaker-topic", data=sneaker)
    # return valid data
    return data


@router.get(
    path="/detail/article/",
    status_code=status.HTTP_200_OK,
    response_model=List[SneakerDetail],
    summary="Get sneaker by href yourself",
)
@cache()
async def get_sneaker_detail_by_article(article: str) -> List[SneakerDetail]:
    """
    Endpoint which get sneaker info by sneaker artile
    :param article:
    :return:
    """
    # get sneaker detail on page by article
    sneaker = get_sneaker_by_article(article=article)
    # validate sneaker data
    data = [
        SneakerDetail(title=title, value=value)
        for title, value in sneaker.items()
    ]
    # check validate data on exist
    check_data_on_exist(validate_data=data)  # type: ignore
    # add valid data into topic
    add_into_topic(topic_name="lamoda-sneaker-topic", data=sneaker)
    # return valid data
    return data
