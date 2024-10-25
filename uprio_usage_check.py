import boto3
import csv
from boto3.dynamodb.conditions import Key

def download_dynamodb_table(table_name, primary_key, primary_key_values, sort_key, date_prefix, region_name, output_file):
    session = boto3.Session(region_name=region_name)
    dynamodb = session.resource('dynamodb')
    table = dynamodb.Table(table_name)
    all_items = []

    for primary_value in primary_key_values:
        response = table.query(
            KeyConditionExpression=Key(primary_key).eq(primary_value) & Key(sort_key).begins_with(date_prefix)
        )

        items = response.get('Items', [])
        all_items.extend(items)

        # Pagination handling
        while 'LastEvaluatedKey' in response:
            response = table.query(
                KeyConditionExpression=Key(primary_key).eq(primary_value) & Key(sort_key).begins_with(date_prefix),
                ExclusiveStartKey=response['LastEvaluatedKey']
            )
            items = response.get('Items', [])
            all_items.extend(items)

        print(f"Downloaded {len(items)} items for {primary_key} = {primary_value}")

    if all_items:
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = all_items[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_items)
        
        print(f"Total of {len(all_items)} items written to {output_file}")

# Example usage
if __name__ == "__main__":
    table_name = 'sdk-usage-audit'
    primary_key = 'audit_id'
    sort_key = 'audit_date'  # Replace with your actual sort key
    primary_key_values = ['praz@uprio.com#usage']  # Add multiple primary key values here
    date_prefix = '2024-09-02'  # Replace with your desired date prefix (e.g., '2024-08-21')
    region_name = 'us-east-1'  # Replace with your AWS region
    output_file = 'uprio_02nd.csv'  # Output CSV file name

    items = download_dynamodb_table(table_name, primary_key, primary_key_values, sort_key, date_prefix, region_name, output_file)
