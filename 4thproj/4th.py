import boto3

s3 = boto3.client('s3', region_name='ap-south-1')

bucket_name = "today-my-newbucket-hh"

s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

print("✅ Bucket created successfully!")


import boto3

s3 = boto3.client('s3', region_name='ap-south-1')

bucket_name = "today-my-newbucket-hh"   # your bucket name
file_path = "test.txt"                  # file in your folder
s3_key = "test.txt"                    # name in S3

s3.upload_file(file_path, bucket_name, s3_key)

print("✅ File uploaded successfully!")



import boto3

ec2 = boto3.resource('ec2', region_name='ap-south-1')

instance = ec2.create_instances(
    ImageId='ami-0e12ffc2dd465f6e4',  # ✅ your AMI
    MinCount=1,
    MaxCount=1,
    InstanceType='t3.micro',
    KeyName='my-key'       # ⚠️ replace this
)

print("✅ EC2 Instance Launched:", instance[0].id)