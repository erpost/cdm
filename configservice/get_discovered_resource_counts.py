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

client = boto3.client('config')
response = client.get_discovered_resource_counts()
resource_counts = response['resourceCounts']
# pprint(resource_counts)

for resource_count in resource_counts:
    print(resource_count['resourceType'])
    resource_list = list(resource_count.values())
    print(resource_list)
