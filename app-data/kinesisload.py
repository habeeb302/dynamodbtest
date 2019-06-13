import boto3
import json
from datetime import datetime
import calendar
import random
import time
import csv
my_stream_name = 'feature_stream'

kinesis_client = boto3.client('kinesis', region_name='ap-southeast-2')
s3 = boto3.client('s3')
def kinesis_write(event,context):

    obj = s3.get_object(Bucket='featuresample', Key='sample_data3.csv')
    rows1 = obj['Body'].read().splitlines()
#   csvfile =  csv.DictReader(rows1)
    data1 = []

    for rows in rows1[1:]:
        x = json.dumps(rows.decode('utf-8')).split(',')
        entity_id = str(x[0])
        updated_time = str(x[1])
        feature_name = str(x[2])
        value = str(x[3])
        y = '{ "entity_id": ' + entity_id + '"' + ','  \
            + ' "updated_time": ' + '"' + updated_time + '"' + ',' \
            + ' "feature_name": ' + '"' + feature_name + '"' + ',' \
            + ' "value": ' + '"' +  value + '"' + '}'
        data1.append(y)
    data2 = str(data1).replace("'","")
    print(data2)




    response = kinesis_client.describe_stream(StreamName=my_stream_name)
    print(response)

    put_response = kinesis_client.put_record(
                        StreamName=my_stream_name,
                        Data=data2,
                        PartitionKey='feature')
    print(put_response)

kinesis_write('','')

