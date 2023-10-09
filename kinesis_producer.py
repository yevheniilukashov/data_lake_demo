import json
import base64
import json
from datetime import datetime, timedelta
import time
import boto3


firehose_client = boto3.client('firehose', region_name='eu-west-1')

def encode(message):
    message_bytes = message.encode('ascii')
    return str(base64.b64encode(message_bytes))[2:-1]



current_date = datetime.now()
for client_number in range(50000):
    for inputType in ['cars', 'apartments', 'memory', 'visitors']:
        client_name = 'client' + str(client_number)
        records = [
            {'Data': json.dumps({'inputType': inputType, 'client_id': encode(client_name), 'time': str(round(time.time() * 1000)), 'value': str(client_number)})}
        ]
        print(records)
        response = firehose_client.put_record_batch(
            DeliveryStreamName='data-platform-dynamic',
            Records=records
        )
        print(response)



def _lambda_responce(code, message):
    return {
        "statusCode": code,
        "body": json.dumps({'message': message})
    }


def lambda_handler(event, context):
    return _lambda_responce(200, event)
