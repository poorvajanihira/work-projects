import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

# Access the table
table = dynamodb.Table('mytable')

# Put an item into the table
response = table.put_item(
    Item={
        'username': 'ENT02',  # Adjust the key names as needed
        'first_name': 'Sekar',
        'last_name': 'Ajith',
        'is_deleted': False,
        'is_good': True
    }
)

# Wait until the table exists (though this is typically not necessary after putting an item)
table.wait_until_exists()

print("PutItem succeeded:", response)
# Print out some data about the table.
#print(table.item_count)
