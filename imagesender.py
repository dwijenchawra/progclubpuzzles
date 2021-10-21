import base64
import boto3
import json
import random

s3 = boto3.client('s3')

def lambda_handler(event, context):
    response = s3.get_object(
        Bucket='fhsprogramminghunt',
        Key='cover-secret.png',
    )
    image = response['Body'].read()
    return {
        'headers': { "Content-Type": "image/png" },
        'statusCode': 200,
        'body': base64.b64encode(image).decode('utf-8'),
        'isBase64Encoded': True
    }
