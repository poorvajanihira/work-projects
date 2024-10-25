import boto3
import csv
from boto3.dynamodb.conditions import Key
from dynamodb_json import json_util as json

def download_dynamodb_table(table_name, primary_key, primary_key_values, region_name, output_file):
    # Initialize a session using Amazon DynamoDB with the specified region
    session = boto3.Session(region_name=region_name)

    # Initialize DynamoDB resource
    dynamodb = session.resource('dynamodb')

    # Select your DynamoDB table
    table = dynamodb.Table(table_name)

    all_items = []

    for value in primary_key_values:
        # Query the table based on the primary key
        response = table.query(
            KeyConditionExpression=Key(primary_key).eq(value)
        )

        # Check if there are any items found
        if 'Items' in response:
            items = json.loads(json.dumps(response['Items'])) 
            print(f"Downloaded {len(items)} items from the table '{table_name}' where {primary_key} = {value}")
            all_items.extend(items)
        else:
            print(f"No items found with {primary_key} = {value} in table '{table_name}'")

    # Write items to CSV file
    if all_items:
        with open(output_file, 'w', newline='') as csvfile:
            # Get the header from the first item's keys
            fieldnames = all_items[0].keys()

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_items)
        
        print(f"Data has been written to {output_file}")

# Example usage
if __name__ == "__main__":
    table_name = 'decode-workspace-usage-aggregation'
    primary_key = 'workspace_id'
    primary_key_values = ['b3b575e4-dfde-47f2-8504-b62d1a6f8759','5bd90942-acb2-46ba-b6a7-90cf728aded3','01GXTWNZPD4ZW6SA1A2B3CA78D']  # Add multiple key values here
    region_name = 'ap-south-1'  # Replace with your AWS region
    output_file = 'usage_data.csv'  # Output CSV file name

    items = download_dynamodb_table(table_name, primary_key, primary_key_values, region_name, output_file)