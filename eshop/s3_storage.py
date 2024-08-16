import boto3
from config import S3_ACCESS_KEY,S3_ENDPOINT_URL,S3_REGION_NAME,S3_SECRET_ACCESS_KEY,S3_BUCKET

session = boto3.Session(
    aws_access_key_id=f"{S3_ACCESS_KEY}",
    aws_secret_access_key=f"{S3_SECRET_ACCESS_KEY}",
    region_name= f"{S3_REGION_NAME}"
)

s3 = session.resource('s3',endpoint_url=f"{S3_ENDPOINT_URL}")
bucket = s3.Bucket(f"{S3_BUCKET}")

async def s3_upload(contents: bytes, key: str):
    bucket.put_object(Key=key, Body=contents)