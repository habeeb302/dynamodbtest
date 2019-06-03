from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr


def dynamoread(event,context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('feature-value-dynamodb')
#   feature_name = 'hours_reg_to_aggregation_lifetime'
    print("read the data from dynamodb table")
    list = []
    response = table.query( KeyConditionExpression=Key('entity_id').eq('022c7afb-dfff-483c-9570-3cdfa6478a80') )
    list.append(response['Items'])
    print(list)

    list_json =  json.dumps(list)
    return list_json

dynamoread('','')