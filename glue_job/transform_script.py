import boto3
import pandas as pd
from io import StringIO

s3 = boto3.client('s3')

def transform_data(bucket, input_key, output_key):
    obj = s3.get_object(Bucket=bucket, Key=input_key)
    df = pd.read_csv(obj['Body'])

    df['total'] = df['price'] * df['quantity']

    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    s3.put_object(Bucket=bucket, Key=output_key, Body=csv_buffer.getvalue())

if __name__ == "__main__":
    transform_data("my-bucket", "input/data.csv", "output/transformed.csv")
