import json
import os
import boto3

CLIENT = boto3.client('firehose', region_name=os.environ['REGION'])


def _lambda_responce(code, message):
    return {
        "statusCode": code,
        "body": json.dumps({'message': message})
    }


def lambda_handler(event, context):
    dict_event = json.loads(event['body'])
    records = [{'Data': json.dumps(dict_event)}]
    response = CLIENT.put_record_batch(
        DeliveryStreamName=os.environ['FIREHOSE'],
        Records=records
    )
    return _lambda_responce(200, response)
