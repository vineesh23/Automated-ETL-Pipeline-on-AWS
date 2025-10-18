import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    glue = boto3.client('glue')

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    print(f"File uploaded: {key} in bucket: {bucket}")

    response = glue.start_job_run(JobName='my-etl-job')
    print(f"Started Glue Job: {response['JobRunId']}")

    return {"statusCode": 200, "body": json.dumps("Glue ETL triggered successfully!")}
