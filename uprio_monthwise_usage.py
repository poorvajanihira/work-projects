import boto3
import csv
from boto3.dynamodb.conditions import Key

def download_dynamodb_table(table_name, primary_key, primary_key_values, sort_key, start_date, end_date, region_name, output_file):
    session = boto3.Session(region_name=region_name)
    dynamodb = session.resource('dynamodb')
    table = dynamodb.Table(table_name)
    all_items = []

    for primary_value in primary_key_values:
        response = table.query(
            KeyConditionExpression=Key(primary_key).eq(primary_value) & Key(sort_key).between(start_date, end_date)
        )
        all_items.extend(response['Items'])

        while 'LastEvaluatedKey' in response:
            response = table.query(
                KeyConditionExpression=Key(primary_key).eq(primary_value) & Key(sort_key).between(start_date, end_date),
                ExclusiveStartKey=response['LastEvaluatedKey']
            )
            all_items.extend(response['Items'])

        print(f"Downloaded {len(all_items)} items from the table '{table_name}' where {primary_key} = {primary_value} between {start_date} and {end_date}")

    if all_items:
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = all_items[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_items)
        
        print(f"Data has been written to {output_file}")

# Example usage
if __name__ == "__main__":
    table_name = 'sdk-usage-audit'
    primary_key = 'audit_id'
    sort_key = 'audit_date'  # Use the appropriate sort key
    primary_key_values = ['praz@uprio.com#usage']
    start_date = '2024-10-17T00:00:00.000000+0000'  # Start of the date range
    end_date = '2024-10-24T23:59:59.999999+0000'  # End of the date range
    region_name = 'us-east-1'
    output_file = 'oct_usage.csv'

    items = download_dynamodb_table(table_name, primary_key, primary_key_values, sort_key, start_date, end_date, region_name, output_file)
