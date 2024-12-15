import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

# Name of the bucket
bucket_name = 'rubysamplebucket'

# File path in S3
file_key = 'ruby.txt'

# Dounload the file in a temporary loction 
s3.download_file(bucket_name, file_key, '/tmp/ruby.txt')

# Read and print the file contents
with open('/tmp/ruby.txt', 'r') as file:
    contents = file.read()
    print(contents)