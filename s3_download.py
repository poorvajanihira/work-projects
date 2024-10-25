import boto3
import os
from urllib.parse import urlparse
from botocore.exceptions import ClientError

def download_s3_files(s3_uris, download_directory):
    # Initialize a session using Amazon S3
    s3 = boto3.client('s3')
    
    # Create download directory if it does not exist
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)

    for s3_uri in s3_uris:
        # Parse S3 URI to get bucket and key
        parsed_url = urlparse(s3_uri)
        bucket_name = parsed_url.netloc
        key = parsed_url.path.lstrip('/')
        
        # Extract file name from key
        file_name = os.path.basename(key)
        file_path = os.path.join(download_directory, file_name)
        
        try:
            # Download file from S3
            print(f"Downloading {s3_uri} to {file_path} ...")
            s3.download_file(bucket_name, key, file_path)
            print(f"Downloaded: {file_name}")
        
        except ClientError as e:
            if e.response['Error']['Code'] == '404':
                print(f"Error: The object {s3_uri} does not exist.")
            else:
                print(f"Failed to download {s3_uri}: {e}")
            continue  # Skip to the next file

# List of S3 URIs
s3_uris = [
's3://in.prod.media.getdecode.io/tester_media/video/a7f69969-3c17-4dd8-9564-e82013016116/01J85KMA79WM1YF5R8YE4DRTQW/d1526ddf-7e52-4830-a24c-fb6a15ddeec6/07b9942c-ccc3-4140-9ddb-1357ab79d6fa/008cca3f-0c3b-4993-a974-50ef394a0a7c/01J85KMA79WM1YF5R8YE4DRTQW.webm',
's3://in.prod.media.getdecode.io/tester_media/video/a7f69969-3c17-4dd8-9564-e82013016116/01J85H3EJF49ZE6BW4PW0JH23J/d1526ddf-7e52-4830-a24c-fb6a15ddeec6/07b9942c-ccc3-4140-9ddb-1357ab79d6fa/16b63105-0792-424c-b22a-7c28c981755d/01J85H3EJF49ZE6BW4PW0JH23J.webm',
's3://in.prod.media.getdecode.io/tester_media/video/a7f69969-3c17-4dd8-9564-e82013016116/01J80M6C721E0WYJ75ZD74FYKT/d1526ddf-7e52-4830-a24c-fb6a15ddeec6/07b9942c-ccc3-4140-9ddb-1357ab79d6fa/1f359c4c-7c9c-4464-83f4-1f01b9eb7a2e/01J80M6C721E0WYJ75ZD74FYKT.webm',
's3://in.prod.media.getdecode.io/tester_media/video/a7f69969-3c17-4dd8-9564-e82013016116/01J80MWR1GNATGNKDEFN70M5XX/d1526ddf-7e52-4830-a24c-fb6a15ddeec6/07b9942c-ccc3-4140-9ddb-1357ab79d6fa/2ec1cfc1-3d04-4a99-84ab-3d31adb03560/01J80MWR1GNATGNKDEFN70M5XX.webm',
's3://in.prod.media.getdecode.io/tester_media/video/a7f69969-3c17-4dd8-9564-e82013016116/01J85J26Q1M41P1D5NXG2BZCJF/d1526ddf-7e52-4830-a24c-fb6a15ddeec6/07b9942c-ccc3-4140-9ddb-1357ab79d6fa/3f246f8f-cc45-4fe4-b381-c4e29be2c491/01J85J26Q1M41P1D5NXG2BZCJF.webm',
's3://in.prod.media.getdecode.io/tester_media/video/a7f69969-3c17-4dd8-9564-e82013016116/01J80P95GMW4FKQJ7CFT7WMR7V/d1526ddf-7e52-4830-a24c-fb6a15ddeec6/07b9942c-ccc3-4140-9ddb-1357ab79d6fa/431428f2-acde-4f5c-8df7-fb147f32d90a/01J80P95GMW4FKQJ7CFT7WMR7V.webm',
's3://in.prod.media.getdecode.io/tester_media/video/a7f69969-3c17-4dd8-9564-e82013016116/01J85F05BGQRPPA3VVK33GDNJ6/d1526ddf-7e52-4830-a24c-fb6a15ddeec6/07b9942c-ccc3-4140-9ddb-1357ab79d6fa/74c0fd68-27ea-4d3c-b36f-b26681cc3e04/01J85F05BGQRPPA3VVK33GDNJ6.webm',
's3://in.prod.media.getdecode.io/tester_media/video/a7f69969-3c17-4dd8-9564-e82013016116/01J85JNDBABXT3ARWEPVBMGSEY/d1526ddf-7e52-4830-a24c-fb6a15ddeec6/07b9942c-ccc3-4140-9ddb-1357ab79d6fa/87451439-a61c-491c-9083-da574e3b58c8/01J85JNDBABXT3ARWEPVBMGSEY.webm',
's3://in.prod.media.getdecode.io/tester_media/video/a7f69969-3c17-4dd8-9564-e82013016116/01J85KG3NCD48R42XBAFY4DNBK/d1526ddf-7e52-4830-a24c-fb6a15ddeec6/07b9942c-ccc3-4140-9ddb-1357ab79d6fa/ae0b0292-1370-476e-8b3a-ec5223942c3c/01J85KG3NCD48R42XBAFY4DNBK.webm',
's3://in.prod.media.getdecode.io/tester_media/video/a7f69969-3c17-4dd8-9564-e82013016116/01J85G15RA360S0FVGGK6KAS11/d1526ddf-7e52-4830-a24c-fb6a15ddeec6/07b9942c-ccc3-4140-9ddb-1357ab79d6fa/b821a05f-74ff-403f-9123-777994b139c8/01J85G15RA360S0FVGGK6KAS11.webm',
's3://in.prod.media.getdecode.io/tester_media/video/a7f69969-3c17-4dd8-9564-e82013016116/01J85F45ZN8VDE10CNY5E51MFV/d1526ddf-7e52-4830-a24c-fb6a15ddeec6/07b9942c-ccc3-4140-9ddb-1357ab79d6fa/ce352cf2-a96e-4e9e-a270-17b8e77270a6/01J85F45ZN8VDE10CNY5E51MFV.webm',
's3://in.prod.media.getdecode.io/tester_media/video/a7f69969-3c17-4dd8-9564-e82013016116/01J85F0MKBCH0KJT5BH7P3PVB4/d1526ddf-7e52-4830-a24c-fb6a15ddeec6/07b9942c-ccc3-4140-9ddb-1357ab79d6fa/e4abc40e-45e4-4ed2-b8e6-7bb2769e0e5b/01J85F0MKBCH0KJT5BH7P3PVB4.webm',
's3://in.prod.media.getdecode.io/tester_media/video/a7f69969-3c17-4dd8-9564-e82013016116/01J85JRHFEKTM271D3XVJV2S0Z/d1526ddf-7e52-4830-a24c-fb6a15ddeec6/07b9942c-ccc3-4140-9ddb-1357ab79d6fa/ec40538f-6d28-4104-8502-d1730db8ce2b/01J85JRHFEKTM271D3XVJV2S0Z.webm',
]

# Directory to download files to
download_directory = './downloaded_files'

# Download the files
download_s3_files(s3_uris, download_directory)
