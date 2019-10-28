import boto3
ec2 = boto3.resource('ec2')

# create a new EC2 instance
instances = ec2.create_instances(
     ImageId='ami-057b5be2c3b9cc63d',
     MinCount=1,
     MaxCount=1,
     InstanceType='t3.nano',
     KeyName='tytoons'
 )
