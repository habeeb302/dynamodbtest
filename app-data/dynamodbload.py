import boto3
import json
import decimal
import datetime

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-2')
print(dynamodb)

table = dynamodb.Table('feature-value-dynamodb')

#with open("moviedata.json") as json_file:
#    movies = json.load(json_file, parse_float = decimal.Decimal)
#    for movie in movies:
#        year = int(movie['year'])
#        title = movie['title']
#        info = movie['info']

print("Adding features:")

table.put_item(
    Item={
        'entity_id': 'user1',
        'feature_name': 'feature1',
        'value': '10',
        'updated_time' : '2019-05-31'
        }
    )
