import json

def _lambda_responce(code, message):
    return {
        "statusCode": code,
        "body": json.dumps({'message': message})
    }


def lambda_handler(event, context):
    return _lambda_responce(200, event)
