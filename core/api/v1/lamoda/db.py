from typing import Dict, List, Union

from fastapi import APIRouter, BackgroundTasks, HTTPException
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
    background_tasks,
    count_objects_in_topic,
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
    response_model=List,
    summary="Get list sneakers on page from db",
)
async def get_list_sneakers_from_db(
    session: ClientSession = get_db_session,
    tasks: BackgroundTasks = background_tasks,
) -> Union[List, ORJSONResponse]:
    """
    Endpoint which get list sneakers from db
    :return:
    """
    try:
        # get valid data from topic
        topic_data = get_data_from_topic(
            topic_name="lamoda-list-sneakers-topic"
        )
        # check data on exits into db
        check_data_on_exits_into_db(
            data=topic_data, collection=lamoda_list_sneakers, session=session
        )
        # work background task
        tasks.add_task(count_objects_in_topic, collection=lamoda_list_sneakers)
        # return all data from collection
        return get_all_doc_form_collection(collection=lamoda_list_sneakers)
    except HTTPException as e:
        return ORJSONResponse(
            status_code=e.status_code, content=f"Error: {str(e)}"
        )
    except Exception as e:
        return ORJSONResponse(status_code=500, content=f"Error: {str(e)}")


@router.get(
    path="/hrefs",
    status_code=status.HTTP_200_OK,
    response_model=List,
    summary="Get list sneaker hrefs on page from db",
)
async def get_list_sneaker_hrefs_from_db(
    session: ClientSession = get_db_session,
    tasks: BackgroundTasks = background_tasks,
) -> Union[List, ORJSONResponse]:
    """
    Endpoint which get list sneaker hrefs from db
    :return:
    """
    try:
        # get valid data from topic
        topic_data = get_data_from_topic(
            topic_name="lamoda-list-sneaker-hrefs-topic"
        )
        # check data on exits into db
        check_data_on_exits_into_db(
            data=topic_data,
            collection=lamoda_list_sneaker_hrefs,
            session=session,
        )
        # work background task
        tasks.add_task(
            count_objects_in_topic, collection=lamoda_list_sneaker_hrefs
        )
        # return all data from collection
        return get_all_doc_form_collection(
            collection=lamoda_list_sneaker_hrefs
        )
    except HTTPException as e:
        return ORJSONResponse(
            status_code=e.status_code, content=f"Error: {str(e)}"
        )
    except Exception as e:
        return ORJSONResponse(status_code=500, content=f"Error: {str(e)}")


@router.get(
    path="/details",
    status_code=status.HTTP_200_OK,
    response_model=List,
    summary="Get list sneaker details by href from db",
)
async def get_list_sneaker_detail_from_db(
    session: ClientSession = get_db_session,
    tasks: BackgroundTasks = background_tasks,
) -> Union[List, ORJSONResponse]:
    """
    Endpoint which get list sneaker details from db
    :return:
    """
    try:
        # get valid data from topic
        topic_data = get_data_from_topic(topic_name="lamoda-sneaker-topic")
        # check data on exits into db
        check_data_on_exits_into_db(
            data=topic_data, collection=lamoda_sneaker_detail, session=session
        )
        # work background task
        tasks.add_task(
            count_objects_in_topic, collection=lamoda_sneaker_detail
        )
        # return all data from collection
        return get_all_doc_form_collection(collection=lamoda_sneaker_detail)
    except HTTPException as e:
        return ORJSONResponse(
            status_code=e.status_code, content=f"Error: {str(e)}"
        )
    except Exception as e:
        return ORJSONResponse(status_code=500, content=f"Error: {str(e)}")


@router.get(
    path="/details/{id}",
    status_code=status.HTTP_200_OK,
    response_model=Dict,
    summary="Get sneaker detail by id from db",
)
async def get_sneaker_detail_by_page_from_db(
    id: str,
) -> Union[Dict, ORJSONResponse]:
    """
    Endpoint get dict sneaker detail by id from db
    :param id:
    :return:
    """
    try:
        # return all data from collection
        return get_doc_from_collection_by_id(
            collection=lamoda_sneaker_detail, id=id
        )
    except HTTPException as e:
        return ORJSONResponse(
            status_code=e.status_code, content=f"Error: {str(e)}"
        )
    except Exception as e:
        return ORJSONResponse(status_code=500, content=f"Error: {str(e)}")
