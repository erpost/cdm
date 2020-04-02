import boto3
import os

from pprint import pprint

credentials_file = os.path.expanduser('~/.aws/cto/credentials')
config_file = os.path.expanduser('~/.aws/cto/config')

# setup local credentials file
if os.path.isfile(credentials_file):
    os.environ['AWS_SHARED_CREDENTIALS_FILE'] = credentials_file
if os.path.isfile(config_file):
    os.environ['AWS_CONFIG_FILE'] = config_file

client = boto3.client('ssm')
instance_id = 'i-04b09daf1594cb872'
response = client.list_inventory_entries(InstanceId=instance_id, TypeName='AWS:Application')

# pprint(response)

for entries in response['Entries']:
    for a, b in entries.items():
        print(a, ':', b)
    print('\n')
