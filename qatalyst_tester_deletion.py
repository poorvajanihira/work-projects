import boto3

# Initialize a session using Amazon DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')  # Replace 'us-west-2' with your desired region

# Specify your DynamoDB table name
table_name = 'qatalyst-tester-details'

# Get the DynamoDB table
table = dynamodb.Table(table_name)

# Specify the study_id for which you want to update tester_ids
study_id = '9f094411-b175-41c1-bc79-bd0cf2e270b5'  # Replace with your actual study_id

# List of tester_ids to update
tester_ids_to_update = [
'07ea4840-8286-4d99-9fe1-74d8b6741b79',
'0a0af333-93c6-4926-a285-c16e62f495af',
'0e95af83-bcdb-413e-bd73-85e8a96cfdc5',
'13ef1a83-7482-49dc-8dad-b4c76851fc92',
'17d89fd4-7b86-4f74-8002-7ae786ffc3be',
'2b7364bf-6a36-4ef4-b126-373b1791abea',
'2e0b9b7f-3d61-45de-935d-bf7bacaf27c5',
'2e3cd4fb-b751-4bef-af84-24df61ee09d9',
'2fffd37c-7018-4c62-a290-ff74b9330949',
'30c16494-1f11-41c4-a23d-873d8864466c',
'341d68b5-a5f3-499f-8df9-8724ef342521',
'34849997-2fa1-4ade-bffd-38f3e40fd939',
'35304b7f-49b6-4773-8790-cfe2943479a3',
'367d8aeb-8452-4c0d-8ebe-0b31e4f6d3e8',
'4659e54a-394d-4ae5-b750-4a7f018c0f80',
'53220d77-c0db-4af7-a668-fb9915fb3dad',
'5a1420bc-b224-4a08-81be-f3029aab7f8b',
'5d9184af-527c-42b8-82ab-7a35596bd446',
'5fc46d03-39b7-44cd-886e-10743ae3ef6b',
'627c271c-d117-4ccc-906d-8f199cdb85c1',
'67ffea16-f1ce-4626-9049-3600ef4913ec',
'6d6f8b6d-d7f3-45db-831c-f539799fd45b',
'6e07f6f1-9cca-46eb-b5c4-d0095dc2014e',
'720b7987-1b68-49a3-a673-a28a15c61ea1',
'7291ea94-fb08-4b9a-99bd-fd55ec47c630',
'72b1d95e-ace0-4225-8dac-b8308cd5214a',
'74b83a79-0143-4e1e-8ad7-558dbee0a053',
'79135e6f-5f44-41bf-bba5-35093e1fa095',
'7a163a7e-1c85-4f23-803a-0abf2a847c4f',
'7e13fa7a-3a5e-4d3d-b5cd-e06cd035ec84',
'7e60790c-6cdc-4074-8da5-c0aefc079bb9',
'8e53ec32-f36d-4fff-ba3a-55c96a343053',
'98d9e613-ee5f-43a9-9c01-e2d47a4e0556',
'99c8031f-ebf6-45b0-9715-bd0f70f0f5a3',
'9aa26cda-a695-4063-ab90-b4f651fa249f',
'a0908e45-5f52-4550-82f1-c05ebdb95709',
'a30c408d-d293-4ea1-9e2e-ffaeab02e14d',
'a34bb25c-e407-4c78-a130-fbe104dba00a',
'a763f540-449d-4f5f-8489-825b6ab1fcb0',
'acf19709-2542-4245-b5b2-578b7dd19806',
'aeb89cc8-4314-4d37-89c6-ebbd656b5d99',
'afaf11ec-aa52-4e25-a9a0-49650deb9bc2',

    # Add more tester_ids as needed
]

# Update the preview attribute to True for the specified tester_ids
for tester_id in tester_ids_to_update:
    response = table.update_item(
        Key={
            'study_id': study_id,
            'tester_id': tester_id
        },
        UpdateExpression="SET preview = :val",
        ExpressionAttributeValues={
            ':val': True
        },
        ReturnValues="UPDATED_NEW"
    )
    print(f"Updated tester_id {tester_id} in study_id {study_id} with response: {response}")

print("Batch update completed!")
