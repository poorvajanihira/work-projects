import json

# Specify the path to your local JSON file
file_path = 'testers_data.json'

# Load JSON data from the file
with open(file_path, 'r') as file:
    testers = json.load(file)

# Filter testers where preview is True and check if 'preview' field exists
testers_with_preview = [tester for tester in testers if tester.get('preview') == True]

# Print only tester_id of filtered testers
if testers_with_preview:
    print("Tester IDs with preview=True:")
    for tester in testers_with_preview:
        print(tester.get('tester_id'))
else:
    print("No testers found with preview=True")

# (Optional) Write the filtered tester IDs to a new JSON file
output_file_path = 'testers_with_preview.json'
with open(output_file_path, 'w') as file:
    json.dump([tester.get('tester_id') for tester in testers_with_preview], file, indent=4)

print(f'Filtered tester IDs have been saved to {output_file_path}')