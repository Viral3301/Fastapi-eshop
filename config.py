import os

from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

DB_HOST_TEST = os.environ.get("DB_HOST_TEST")
DB_PORT_TEST = os.environ.get("DB_PORT_TEST")
DB_NAME_TEST = os.environ.get("DB_NAME_TEST")
DB_USER_TEST = os.environ.get("DB_USER_TEST")
DB_PASS_TEST = os.environ.get("DB_PASS_TEST")

REDIS_HOST = os.environ.get("REDIS_HOST")

S3_URL = os.environ.get("S3_URL")

S3_ACCESS_KEY = os.environ.get("S3_ACCESS_KEY")

S3_SECRET_ACCESS_KEY = os.environ.get("S3_SECRET_ACCESS_KEY")

S3_ENDPOINT_URL = os.environ.get("S3_ENDPOINT_URL")

S3_REGION_NAME = os.environ.get("S3_REGION_NAME")

S3_BUCKET = os.environ.get("S3_BUCKET")