import boto3
ec2 = boto3.resource('ec2')

# create a new EC2 instance
instances = ec2.create_instances(
     ImageId='ami-03dbf9550d4620230',
     MinCount=1,
     MaxCount=1,
     InstanceType='t2.micro',
     KeyName='aws-windows',
     NetworkInterfaces=[{
         'SubnetId': 'subnet-05bd2cc86c1e09ec5',
         'DeviceIndex': 0,
         'AssociatePublicIpAddress': True,
         'Groups':['sg-03bc17a19529ccc88'],
         }]
 )
print('Successfully launched EC2 Instance')
