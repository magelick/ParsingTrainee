from typing import Dict, List

from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from pymongo.client_session import ClientSession
from starlette import status

from core.database.base import (
    lamoda_sneaker_detail,
    lamoda_list_sneakers,
    lamoda_list_sneaker_hrefs,
)
from core.dependencies import (
    get_all_doc_form_collection,
    get_doc_from_collection_by_id,
    get_db_session,
    get_data_from_topic,
    check_data_on_exits_into_db,
)

# lamoda db router
router = APIRouter(
    prefix="/lamoda/db",
    default_response_class=ORJSONResponse,
    tags=["Lamoda DB"],
)


@router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    summary="Get list sneakers on page from db",
)
async def get_list_sneakers_from_db(
    session: ClientSession = get_db_session,
) -> List:
    """
    Endpoint which get list sneakers from db
    :return:
    """
    topic_data = get_data_from_topic(topic_name="lamoda-list-sneakers-topic")
    check_data_on_exits_into_db(
        data=topic_data, collection=lamoda_list_sneakers, session=session
    )
    return get_all_doc_form_collection(collection=lamoda_list_sneakers)


@router.get(
    path="/hrefs",
    status_code=status.HTTP_200_OK,
    summary="Get list sneaker hrefs on page from db",
)
async def get_list_sneaker_hrefs_from_db(
    session: ClientSession = get_db_session,
) -> List:
    """
    Endpoint which get list sneaker hrefs from db
    :return:
    """
    topic_data = get_data_from_topic(
        topic_name="lamoda-list-sneaker-hrefs-topic"
    )
    check_data_on_exits_into_db(
        data=topic_data, collection=lamoda_list_sneaker_hrefs, session=session
    )
    return get_all_doc_form_collection(collection=lamoda_list_sneaker_hrefs)


@router.get(
    path="/details",
    status_code=status.HTTP_200_OK,
    summary="Get list sneaker details by href from db",
)
async def get_list_sneaker_detail_from_db(
    session: ClientSession = get_db_session,
) -> List:
    """
    Endpoint which get list sneaker details from db
    :return:
    """
    topic_data = get_data_from_topic(topic_name="lamoda-sneaker-topic")
    check_data_on_exits_into_db(
        data=topic_data, collection=lamoda_sneaker_detail, session=session
    )
    return get_all_doc_form_collection(collection=lamoda_sneaker_detail)


@router.get(
    path="/{id}",
    status_code=status.HTTP_200_OK,
    summary="Get sneaker detail by id from db",
)
async def get_sneaker_detail_by_page_from_db(id: str) -> Dict:
    """
    Endpoint get dict sneaker detail by id from db
    :param id:
    :return:
    """
    return get_doc_from_collection_by_id(
        collection=lamoda_sneaker_detail, id=id
    )
