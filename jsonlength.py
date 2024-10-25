import os
import json

def get_json_list_length(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return len(data)

def iterate_directory(directory_path):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path) and file_path.endswith('.json'):
            try:
                length = get_json_list_length(file_path)
                print(f"File: {filename}, List length: {length}")
            except (json.JSONDecodeError, KeyError):
                print(f"File: {filename}, Error: Not a valid JSON file or incorrect structure")

# Specify your directory path here
directory_path = './path_to_your_directory'
iterate_directory(directory_path)