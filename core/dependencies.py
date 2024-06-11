import json
import uuid
from typing import Dict, List

import requests
from bs4 import BeautifulSoup
from fastapi import Depends
from pykafka.common import OffsetType
from pymongo.client_session import ClientSession
from requests import Response
from pymongo.collection import Collection

from core.database.base import client
from core.settings import client as kafka_client


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
    data["_id"] = str(uuid.uuid4())
    collection.insert_one(document=data, session=session)


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


def add_into_topic(topic_name: str, data: dict):
    """
    Func which add data into topic
    :param topic_name:
    :param data:
    :return:
    """
    topic = kafka_client.topics[topic_name]
    with topic.get_producer() as producer:
        producer.produce(json.dumps(data).encode("utf-8"))


def get_data_from_topic(topic_name) -> Dict:
    """
    Func which get data from topic
    :param topic_name:
    :return:
    """
    topic = kafka_client.topics[topic_name]
    consumer = topic.get_simple_consumer(
        consumer_group=b"my_group",
        consumer_timeout_ms=10,
        auto_offset_reset=OffsetType.LATEST,
    )
    data = {}
    message = consumer.consume()
    if message is not None:
        data[str("kafka_data")] = message.value.decode("utf-8")
        consumer.commit_offsets()
    return data


def check_data_on_exits_into_db(
    data: dict, collection: Collection, session: ClientSession
):
    """
    Func which check data on exits into db
    :param data:
    :param collection:
    :param session:
    :return:
    """
    existing_data = get_all_doc_form_collection(collection=collection)
    for doc in existing_data:
        if doc.get("kafka_data") == data.get("kafka_data"):
            return
    add_doc_into_collection(collection=collection, data=data, session=session)


def _get_db_session():
    """
    Depends which get session to db
    :return:
    """
    with client.start_session() as session:
        yield session


# Initial Depends
get_db_session = Depends(_get_db_session)
