import boto3
from boto3.dynamodb.conditions import Key, Attr
import pandas as pd

# Get the DynamoDB service resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('qatalyst-tester-details')

# Scan the table with filter conditions
response = table.query(
    KeyConditionExpression=Key('study_id').eq('58c4f2ce-263d-4019-9ec5-826b6daea6da'),
    FilterExpression=Attr('tester_name').contains('Abha Asthana')
)
items = response['Items']

# Print a message showing how many items were retrieved
print(f"Fetched {len(items)} items from the table:")

# Convert the fetched items to a pandas DataFrame if needed
df = pd.DataFrame(items)

# Save the DataFrame to a CSV file if desired
output_file = 'lucknow_items.csv'
df.to_csv(output_file, index=False)

print(f"Data successfully saved to {output_file}")