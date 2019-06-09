import boto3
import json
import decimal
import datetime
import csv

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

obj = s3.get_object(Bucket='featuresample',Key='sample_data3.csv')
rows1 = obj['Body'].read().decode("utf-8")
rows = rows1.split('\n')


table = dynamodb.Table('feature-value-dynamodb')

#with open("moviedata.json") as json_file:
#    movies = json.load(json_file, parse_float = decimal.Decimal)
#    for movie in movies:
#        year = int(movie['year'])
#        title = movie['title']
#        info = movie['info']


print("Adding features:")
with table.batch_writer() as batch:

  for row in rows[1:]:
      print(row)
      entity_id = row.split(',')[0]
      feature_name = row.split(',')[2]
      value = row.split(',')[3]
      updated_time = row.split(',')[1]
      batch.put_item(
       Item={
        'entity_id': entity_id,
        'feature_name': feature_name,
        'value': value,
        'updated_time' : updated_time
             }
      )
