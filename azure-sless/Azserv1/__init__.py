import logging

import azure.functions as func
import requests
from azure.cosmos import CosmosClient, PatitionKey


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    numbers = requests.get('').text
    letters = requests.get('').text

    username = ''
    for i in range (5):
        username += numbers[i]
        username += letters[i]

    key = ''
    endpoint = ''

    client = CosmosClient(endpoint, key)

    database_name = "Usernames"
    database = client.create_database_if_not_exists(id=database_name)

    container_name = "UsernameCont"
    container = database.create_container_if_not_exists(
        id=container_name,
        Partition_key=PartitionKey(path="/username") 
    )
    username_to_add = {
        "id": username
    }
    container.create_iteam(body=username_to_add)
    return username
