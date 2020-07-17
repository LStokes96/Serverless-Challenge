import logging

import azure.functions as func

import random


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    number = str(random.randint(10000, 99999))
    return number
