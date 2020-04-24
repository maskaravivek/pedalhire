from ..constants.env_constants import GOOGLE_CLOUD_BUCKET


def upload_blob(source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(GOOGLE_CLOUD_BUCKET)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)
    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )
