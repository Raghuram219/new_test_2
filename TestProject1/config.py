import os
import json
import boto3
from dotenv import load_dotenv
from botocore.exceptions import ClientError

# Load local .env values
load_dotenv()

# Environment Type
ENV_TYPE = os.getenv("ENV_TYPE", "nonlocal")


class Config:
    """
    Centralized configuration management
    Supports:
    - Local .env
    - AWS Secrets Manager
    """

    # Default values from .env
    NAME = os.getenv("NAME")
    USER = os.getenv("USER")
    PASSWORD = os.getenv("PASSWORD")
    HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")

    # Local Development
    if ENV_TYPE == "local":


        print("Running in LOCAL environment")

        HOST = "localhost"

    # AWS Environment
    else:

        print(f"Running in {ENV_TYPE.upper()} environment")

        SECRET_NAME = os.getenv("AWS_SECRET_NAME","dev/Test/env")
        AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

        try:
            session = boto3.session.Session()

            client = session.client(
                service_name="secretsmanager",
                region_name=AWS_REGION
            )

            response = client.get_secret_value(
                SecretId=SECRET_NAME
            )

            secret = response["SecretString"]

            # Convert JSON string to dictionary
            secret_data = json.loads(secret)

            # Override values from AWS Secrets Manager
            NAME = secret_data.get("NAME")
            USER = secret_data.get("USER")
            PASSWORD = secret_data.get("PASSWORD")
            HOST = secret_data.get("HOST")
            PORT = secret_data.get("PORT")

            print("AWS Secrets Loaded Successfully")

        except ClientError as error:

            print("Failed to fetch AWS Secret")
            raise error