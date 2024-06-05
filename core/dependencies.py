import uuid
from typing import Dict, List

import requests
from bs4 import BeautifulSoup
from fastapi import Depends
from pymongo.client_session import ClientSession
from requests import Response
from pymongo.collection import Collection

from core.database.base import client


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


def add_doc_into_collection(
    collection: Collection, data: dict, session: ClientSession
):
    """
    Func which add data into collection
    :param collection:
    :param data:
    :param session:
    :return:
    """
    data["_id"] = str(uuid)
    return collection.insert_one(document=data, session=session)


def get_all_doc_form_collection(collection: Collection) -> List[Dict]:
    """
    Func which get all data from collection
    :param collection:
    :return:
    """
    return list(collection.find())


def get_doc_from_collection_by_id(collection: Collection, id: str):
    """
    Func which get data from collection by id
    :param collection:
    :param id:
    :return:
    """
    return collection.find_one({"_id": str(id)})


def delete_doc_form_collection_by_id(
    collection: Collection, id: str, session: ClientSession
):
    """
    Func which delete data from collection by id
    :param collection:
    :param id:
    :param session:
    :return:
    """
    collection.delete_one({"_id": str(id)}, session=session)


def check_data_on_exist(validate_data: dict):
    """
    Func which check data on exist
    :param validate_data:
    :return:
    """
    if not validate_data:
        raise ValueError("Invalid Data")


def _get_db_session():
    """
    Depends which get session to db
    :return:
    """
    with client.start_session() as session:
        yield session


# Initial Depends
get_db_session = Depends(_get_db_session)
