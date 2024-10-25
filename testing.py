import json
import csv

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

# Define the path to your JSON file and CSV output
json_file_path = 'Sample_data.json'  # Replace with your JSON file path
csv_file_path = 'output.csv'  # Replace with your desired CSV file path

# Read the JSON file
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# If the JSON is a dictionary, try to convert it into a list of dictionaries
if isinstance(data, dict):
    data = [flatten_json(data)]

# If it's a list of dictionaries, flatten each item
elif isinstance(data, list):
    data = [flatten_json(item) for item in data]

# Now we proceed with writing to CSV if data is a list of dictionaries
if isinstance(data, list):
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
        
    print(f"CSV file '{csv_file_path}' created successfully.")
else:
    print("JSON file does not contain a list of dictionaries.")