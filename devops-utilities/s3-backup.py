"""
This is a script to take a backup from local to AWS S3
boto3 -> used to do AWS tasks using Python
"""

import boto3
from botocore.exceptions import ClientError

# create a boto3 resource for s3
s3 = boto3.resource("s3")


def show_buckets(s3_resource):
    """Print all bucket names for the given s3 resource."""
    for bucket in s3_resource.buckets.all():
        print(bucket.name)


def create_bucket(s3_resource, bucket_name, region=None):
    """
    Create an S3 bucket in specified region.
    Note: For us-east-1 the CreateBucketConfiguration must not be sent.
    """
    try:
        if region is None or region == "us-east-1":
            s3_resource.create_bucket(Bucket=bucket_name)
        else:
            s3_resource.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={"LocationConstraint": region},
            )
        print(f"Bucket '{bucket_name}' created successfully.")
    except ClientError as e:
        print(f"Could not create bucket '{bucket_name}': {e}")
        raise


def upload_backup(s3_resource, file_name, bucket_name, key_name):
    """
    Uploads a given backup file path to a given s3 bucket
    with a new name (key).
    """
    try:
        with open(file_name, "rb") as f:
            data = f.read()

        s3_resource.Bucket(bucket_name).put_object(Key=key_name, Body=data)
        print("Backup uploaded successfully.")
    except FileNotFoundError:
        print(f"Local file not found: {file_name}")
        raise
    except ClientError as e:
        print(f"Failed to upload backup to {bucket_name}/{key_name}: {e}")
        raise


if __name__ == "__main__":
    # Example usage (edit file_name and bucket_name as needed)
    bucket_name = "python-for-devops-hareesh"
    region = "us-east-2"

    # Example local file path — replace with your actual backup file
    file_name = "/Users/hareesh/python-workshop/python-workshop-practice/my-backup.tar.gz"
    key_name = "my-backup.tar.gz"

    # Uncomment to create the bucket if you need to
    # create_bucket(s3, bucket_name, region)

    # Uncomment to list buckets
    # show_buckets(s3)

    # Upload the backup
    upload_backup(s3, file_name, bucket_name, key_name)


#type terminal: python python s3_backup.py
#backup script