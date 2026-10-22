import boto3
import os

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    instance_id = os.environ['INSTANCE_IDS'].split(',')
    instance_id = [i.strip() for i in instance_id]

    response = ec2.start_instances(
        InstanceIds=instance_id
    )
    print("EC2 instance started successfully")
    return response