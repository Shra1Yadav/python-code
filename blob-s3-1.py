#This python code is used to move data from azure blob container to AWS S3 bucket
# run this file with this command python3 <file_name>

import os
import boto3
from azure.storage.blob import BlobServiceClient

# Azure Blob Storage credentials
azure_storage_account_name = "testals"
azure_storage_account_key = "dCwtFhI8T0NnTXQkrg/Mt5G62bb4ilPg+F3L46957tT8bXe4yVobrIZUBKDytLpN9K8BoHkWqQYd+AStrCm+nw=="
azure_blob_container_name = "migration-test"

# AWS S3 credentials
aws_access_key_id = "AKIAWSF7RDU6ZUVPGYE3"
aws_secret_access_key = "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"
aws_s3_bucket_name = "azure-migrated"

# Initialize Azure Blob Service Client
azure_blob_service_client = BlobServiceClient(account_url=f"https://{azure_storage_account_name}.blob.core.windows.net",
                                             credential=azure_storage_account_key)

# Initialize AWS S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# List all blobs in the Azure container
container_client = azure_blob_service_client.get_container_client(azure_blob_container_name)
blobs = container_client.list_blobs()

# Copy each blob from Azure Blob Storage to AWS S3 mirroring the folder structure
for blob in blobs:
    blob_name = blob.name
    s3_object_key = blob_name  # Use the same blob name as the S3 object key
    print(f"Copying {blob_name} to S3 as {s3_object_key}")

    # Download the blob from Azure
    blob_client = container_client.get_blob_client(blob_name)
    blob_data = blob_client.download_blob()

    # Upload the blob data to AWS S3
    s3.put_object(Bucket=aws_s3_bucket_name, Key=s3_object_key, Body=blob_data.readall())

print("Data transfer completed.")


