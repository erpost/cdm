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

client = boto3.client('inspector')
response = client.describe_findings(findingArns=[
    'arn:aws:inspector:us-east-2:<account id>:target/0-owPPx7Wp/template/0-BNfXR2YW/run/0-Bu11oIep/finding/0-xp5pazmY',
    'arn:aws:inspector:us-east-2:<account id>:target/0-owPPx7Wp/template/0-BNfXR2YW/run/0-Bu11oIep/finding/0-xcubsTZB']
    )
pprint(response)
