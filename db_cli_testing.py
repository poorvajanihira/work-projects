import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

# Access the table
table = dynamodb.Table('mytable')

# Put an item into the table
response = table.update_item(
    Key={
        'username': 'ENT02',  # Adjust the key names as needed
    },
    UpdateExpression='SET is_delete = :val1',
    ExpressionAttributeValues={
        ':val1':True
)

# Wait until the table exists (though this is typically not necessary after putting an item)
table.wait_until_exists()

print("UpdateItem succeeded:", response)
# Print out some data about the table.
#print(table.item_count)
