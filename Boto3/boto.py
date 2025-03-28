import boto3

# Idempotency
# Create an S3 client
s3_client = boto3.client('s3')


s3_client.create_bucket(Bucket='botobucketskwargs')
s3_client.upload_file('./README.md', 'botobucketskwargs', 'README.md')
s3_client.download_file('botobucketskwargs', 'README.md', 'README2.md')
response = s3_client.list_buckets(
    MaxBuckets=10
)

# print(response)

# EC2 Client

# Global EC2 client
ec2_client = boto3.client("ec2")

def create_ec2_instance():
    response = ec2_client.run_instances(
        ImageId="ami-071226ecf16aa7d96",  # Replace with your AMI ID
        InstanceType="t2.micro",  # Change instance type as needed
        MinCount=1,
        MaxCount=1,
        # KeyName="test",  # Replace with your key pair name
        # SecurityGroupIds=["sg-0123456789abcdef0"],  # Replace with your security group ID
        # SubnetId="subnet-0123456789abcdef0",  # Replace with your subnet ID (if needed)
        TagSpecifications=[
            {
                "ResourceType": "instance",
                "Tags": [{"Key": "Name", "Value": "MyBoto3Instance"}]
            }
        ]
    )
    
    instance_id = response["Instances"][0]["InstanceId"]
    print(f"EC2 Instance {instance_id} is launching...")
    return instance_id

# Call function to create EC2 instance
# instance_id = create_ec2_instance()
# print(instance_id)

# Pagination

filters = [
    {
        "Name": "tag:Name",
        "Values": ["MyBoto3Instance"]
    }
]

def describe_my_instances(filters):
    
    reservations = []
    next_token = None

    while True:
        response = ec2_client.describe_instances(
            Filters=filters,
            MaxResults=1000,
            NextToken=next_token
        ) if next_token else ec2_client.describe_instances(
            Filters=filters,
            MaxResults=1000
        )

        reservations.extend(response.get("Reservations", []))
        next_token = response.get("NextToken")

        if not next_token:
            break

    return reservations

print(describe_my_instances(filters))