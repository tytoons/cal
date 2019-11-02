import sys
import boto3
ec2 = boto3.resource('ec2')

# create a new EC2 instance
instances = ec2.create_instances(
     ImageId = sys.argv[1],
     MinCount = 1,
     MaxCount = 1,
     InstanceType = 't3.nano',
     KeyName = 'tytoons',
     SecurityGroups = ['ec2_node_sg'],
     PrivateIpAddress = sys.argv[2] #elastic_ip
 )
