import boto3
import os


credentials_file = os.path.expanduser('~/.aws/cto/credentials')
config_file = os.path.expanduser('~/.aws/cto/config')

# setup local credentials file
if os.path.isfile(credentials_file):
    os.environ['AWS_SHARED_CREDENTIALS_FILE'] = credentials_file
if os.path.isfile(config_file):
    os.environ['AWS_CONFIG_FILE'] = config_file

client = boto3.client('config')
response = client.get_resource_config_history(
    resourceType='AWS::EC2::Instance',
    resourceId='i-xxxxxxxxxxxxxxxxx')

conf_items = response['configurationItems']
print(conf_items[0]['resourceCreationTime'])
