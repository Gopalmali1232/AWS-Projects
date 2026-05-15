import boto3

region = 'ap-south-1'
s3 = boto3.client('s3', region_name=region)

bucket_name = "hitesh-static-site-12390"

s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': region
    }
)

print("✅ Bucket created")

s3.put_bucket_website(
    Bucket=bucket_name,
    WebsiteConfiguration={
        'IndexDocument': {'Suffix': 'index.html'}
    }
)

print("✅ Website hosting enabled")


s3.put_public_access_block(
    Bucket=bucket_name,
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,
        'IgnorePublicAcls': False,
        'BlockPublicPolicy': False,
        'RestrictPublicBuckets': False
    }
)

import json

policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": f"arn:aws:s3:::{bucket_name}/*"
        }
    ]
}

s3.put_bucket_policy(
    Bucket=bucket_name,
    Policy=json.dumps(policy)
)

print("✅ Bucket policy applied")


import os

folder_path = "."

for file in os.listdir(folder_path):
    if file.endswith(".html") or file.endswith(".css") or file.endswith(".js"):
        s3.upload_file(file, bucket_name, file)
        print(f"Uploaded: {file}")
print("🚀 Website deployed successfully!")




