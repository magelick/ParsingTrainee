import json
import uuid
import time
import datetime
from typing import Dict, List

import requests
from bs4 import BeautifulSoup
from fastapi import Depends, BackgroundTasks
from pykafka import SimpleConsumer
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


def count_objects_in_topic(collection: Collection):
    """
    Func which get count documents into db
    :param collection:
    :return:
    """
    with open("count_collection.txt", mode="a") as log:
        count = collection.count_documents({})
        log.write(
            f"\n{datetime.datetime.now()}: {collection.name} -> {str(count)}"
        )


def get_producer_and_consumer():
    """
    Func which get producers and consumers for all topics
    :return:
    """
    topics = [
        "lamoda-list-sneakers-topic",
        "lamoda-list-sneaker-hrefs-topic",
        "lamoda-sneaker-topic",
        "twitch-auth-topic",
        "twitch-user-topic",
        "twitch-games-topic",
        "twitch-top-games-topic",
        "twitch-games-analytic-topic",
        "twitch-channel-information-topic",
        "twitch-channel-editor-topic",
        "twitch-channel-followed-topic",
        "twitch-channel-followers-topic",
        "twitch-channel-emotes-topic",
        "twitch-channel-chat-settings-topic",
        "twitch-channel-vip-topic",
        "twitch-global-emotes-topic",
        "twitch-clips-topic",
        "twitch-pools-topic",
    ]
    producers = {}
    consumers = {}
    for topic in topics:
        topic_obj = kafka_client.topics[topic]
        producers[topic] = topic_obj.get_producer(delivery_reports=True)
        consumer = SimpleConsumer(
            topic=topic_obj,
            cluster=kafka_client.cluster,
            auto_offset_reset=OffsetType.LATEST,
            consumer_group="my_group",
        )
        consumers[topic] = consumer
    kafka_instances = {"producers": producers, "consumers": consumers}
    return kafka_instances


# Initial Producer and Consumer items
kafka_items = get_producer_and_consumer()


def add_into_topic(topic_name: str, data: dict):
    """
    Func which add data into topic
    :param topic_name:
    :param data:
    :return:
    """
    producer = kafka_items["producers"][topic_name]
    producer.produce(json.dumps(data).encode("utf-8"))


def get_data_from_topic(topic_name, limit=1, timeout=10) -> Dict:
    """
    Func which get data from topic
    :param timeout:
    :param limit:
    :param topic_name:
    :return:
    """
    consumer = kafka_items["consumers"][topic_name]
    data: dict = {}

    if consumer is None:
        return data

    start_time = time.time()
    while limit > 0:
        message = consumer.consume()
        if message is None or not message:
            if time.time() - start_time > timeout:
                break
            else:
                time.sleep(1)
                continue
        data[str("kafka_data")] = json.loads(message.value.decode("utf-8"))
        consumer.commit_offsets()
        limit -= 1

    return data if data else None


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
    if not data:
        return
    existing_data = get_all_doc_form_collection(collection=collection)
    for doc in existing_data:
        if doc.get("kafka_data") == data.get("kafka_data"):
            return
    if not data.get("kafka_data"):
        pass
    else:
        add_doc_into_collection(
            collection=collection, data=data, session=session
        )


def _get_db_session():
    """
    Depends which get session to db
    :return:
    """
    with client.start_session() as session:
        yield session


# Initial Depends
get_db_session = Depends(_get_db_session)
background_tasks = BackgroundTasks()
