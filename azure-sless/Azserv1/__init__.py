import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    num = list(randlet())
    let = list(str(randnum()))
    for n in range (len(let)):
        num.insert(n*2, let[n])
    return num