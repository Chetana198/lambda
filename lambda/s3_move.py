import boto3
import os
import urllib.parse

s3 = boto3.client('s3')
DEST_BUCKET = os.environ['DEST_BUCKET']

def lambda_handler(event, context):
    for record in event['Records']:
        src_bucket = record['s3']['bucket']['name']
        src_key = urllib.parse.unquote_plus(record['s3']['object']['key'])

        copy_source = {'Bucket': src_bucket, 'Key': src_key}
        s3.copy_object(CopySource=copy_source, Bucket=DEST_BUCKET, Key=src_key)
        s3.delete_object(Bucket=src_bucket, Key=src_key)

    return {
        'statusCode': 200,
        'body': f'Moved {src_key} from {src_bucket} to {DEST_BUCKET}'
    }
