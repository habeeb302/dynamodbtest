import boto3
import json
from datetime import datetime
import time
import base64
my_stream_name = 'feature_stream'

kinesis_client = boto3.client('kinesis', region_name='ap-southeast-2')

response = kinesis_client.describe_stream(StreamName=my_stream_name)

my_shard_id = response['StreamDescription']['Shards'][0]['ShardId']

shard_iterator = kinesis_client.get_shard_iterator(StreamName=my_stream_name,
                                                      ShardId=my_shard_id,
                                                      ShardIteratorType='LATEST')
print(shard_iterator)
my_shard_iterator = shard_iterator['ShardIterator']

record_response = kinesis_client.get_records(ShardIterator=my_shard_iterator,
                                              Limit=2)
print(record_response)
while 'NextShardIterator' in record_response:
    record_response = kinesis_client.get_records(ShardIterator=record_response['NextShardIterator'],
                                                  Limit=2)
#    records = base64.b64decode(record_response)
    records1 = record_response['Records']
    print(records1)
    print(record_response)

    # wait for 5 seconds
    time.sleep(5)