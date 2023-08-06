import base64
import json
import pickle

from boto3 import client, resource
from botocore.exceptions import ClientError
from ssm_parameter_store import EC2ParameterStore


def translate(text, source="zh", dest="en"):
    translate_client = client(service_name="translate")
    result = translate_client.translate_text(
        Text=text, SourceLanguageCode=source, TargetLanguageCode=dest
    )
    return result.get("TranslatedText")


def get_secret(secret_id: str):
    secrets_manager = client("secretsmanager")
    try:
        get_secret_value_response = secrets_manager.get_secret_value(SecretId=secret_id)
    except ClientError as e:
        if e.response["Error"]["Code"] == "DecryptionFailureException":
            # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response["Error"]["Code"] == "InternalServiceErrorException":
            # An error occurred on the server side.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response["Error"]["Code"] == "InvalidParameterException":
            # You provided an invalid value for a parameter.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response["Error"]["Code"] == "InvalidRequestException":
            # You provided a parameter value that is not valid for the current state of the resource.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response["Error"]["Code"] == "ResourceNotFoundException":
            # We can't find the resource that you asked for.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
    else:
        # Decrypts secret using the associated KMS CMK.
        # Depending on whether the secret is a string or binary, one of these fields will be populated.
        if "SecretString" in get_secret_value_response:
            secret = get_secret_value_response["SecretString"]
        else:
            secret = base64.b64decode(get_secret_value_response["SecretBinary"])
        return json.loads(secret)


def s3_copy(from_, to):
    s3 = boto3.resource("s3")
    copy_source = {"Bucket": BUCKET_NAME, "Key": from_}
    bucket = s3.Bucket(BUCKET_NAME)
    obj = bucket.Object(to)
    obj.copy(copy_source)


def s3_dump(obj, path, to_pickle=True):
    bucket = BUCKET_NAME
    key = path
    if to_pickle:
        upload_obj = pickle.dumps(obj)
    else:
        upload_obj = obj
    s3_resource = resource("s3")
    s3_resource.Object(bucket, key).put(Body=upload_obj)


def s3_load(path, from_pickle=True):
    bucket = BUCKET_NAME
    key = path
    s3_resource = resource("s3")
    s3_resource.Object(bucket, path)
    response = s3_resource.Object(bucket, key).get()
    if from_pickle:
        return pickle.loads(response["Body"].read())
    else:
        return response["Body"].read()


def s3_exists(path):
    bucket = BUCKET_NAME
    key = path
    s3_resource = resource("s3")
    s3_resource.Object(bucket, path)
    try:
        s3_resource.Object(bucket, key).load()
        return True
    except ClientError as e:
        if e.response["Error"]["Code"] == "404":
            return False
        else:
            raise


def get_ssm_parameter(key):
    store = EC2ParameterStore()
    res = store.get_parameter(key)
    return res[key]
