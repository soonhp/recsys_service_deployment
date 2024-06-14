import os

import boto3
from dotenv import load_dotenv

load_dotenv('.env.dev')


def download_vectordb():
    print(f"Download chroma.sqlite3".ljust(60, '>'))
    s3 = boto3.client(
        service_name="s3",
        region_name="ap-northeast-2",
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
    )
    if not os.path.exists('llmrec/vector_dbs/hyeonwoo'):
        os.makedirs('llmrec/vector_dbs/hyeonwoo')
    if not os.path.exists('llmrec/vector_dbs/hyeonwoo/chroma.sqlite3'):
        s3.download_file(Bucket='pseudorec-data', Key='hyeonwoo/chroma.sqlite3', Filename='llmrec/vector_dbs/hyeonwoo/chroma.sqlite3')

    if not os.path.exists('llmrec/vector_dbs/gyungah'):
        os.makedirs('llmrec/vector_dbs/gyungah')
    if not os.path.exists('llmrec/vector_dbs/hyeonwoo/chroma.sqlite3'):
        s3.download_file(Bucket='pseudorec-data', Key='gyungah/chroma.sqlite3', Filename='llmrec/vector_dbs/gyungah/chroma.sqlite3')


if __name__ == "__main__":
    print(os.getcwd())
    download_vectordb()
