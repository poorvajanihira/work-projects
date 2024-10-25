import boto3

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb')

# Function to query first table
def query_table_1(table_name, partition_key_value):
    table = dynamodb.Table(table_name)
    response = table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key('partition_key').eq(partition_key_value)
    )
    return response['Items']

# Function to query second table
def query_table_2(table_name, foreign_key_value):
    table = dynamodb.Table(table_name)
    response = table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key('foreign_key').eq(foreign_key_value)
    )
    return response['Items']

# Combine data from two tables
def combine_data(data_1, data_2):
    combined_data = []
    for item1 in data_1:
        for item2 in data_2:
            # Combine the records where the common key matches
            if item1['common_key'] == item2['common_key']:
                combined_item = {**item1, **item2}  # Merge dictionaries
                combined_data.append(combined_item)
    return combined_data

# Main execution
if __name__ == "__main__":
    # Query both tables
    data_from_table_1 = query_table_1('Table1', 'some_partition_key_value')
    data_from_table_2 = query_table_2('Table2', 'some_foreign_key_value')

    # Combine the results based on common key
    combined_results = combine_data(data_from_table_1, data_from_table_2)

    # Print the combined data
    for item in combined_results:
        print(item)
