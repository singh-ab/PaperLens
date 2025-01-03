import os
from dotenv import load_dotenv
import boto3


# Load environment variables from the .env file
load_dotenv()

# Get the value of the DATABASE_URL environment variable
DATABASE_URL = os.getenv("DATABASE_URL")


# Create an S3 client using the AWS credentials and region from environment variables
s3_client = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("S3_REGION_NAME")
)

# Get the value of the S3_BUCKET_NAME environment variable
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

import boto3

s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("S3_REGION_NAME")
)
response = s3_client.list_objects_v2(Bucket=os.getenv("S3_BUCKET_NAME"))
print(response)
