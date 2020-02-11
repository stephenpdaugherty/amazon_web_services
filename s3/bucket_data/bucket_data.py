
import boto3
import os


s3_client = boto3.client('s3')
all_buckets = s3_client.list_buckets()
bucket_names = []


for bucket in all_buckets['Buckets']:
    #Get a list of all buckets
    bucket_names.append(bucket['Name'])
    
    
for bucket in bucket_names:
    '''
    For each bucket in the account, return bucket name and size.
    Using AWS CLI command is cleaner and quicker than Boto3 options.
    '''
    cmd = f'aws s3 ls s3://{bucket} --recursive --human-readable --summarize'
    print(f'Bucket Name: {bucket}')
    print('Bucket Information')
    os.system(cmd)
    
