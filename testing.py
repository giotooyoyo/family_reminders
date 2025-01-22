import json

file_path = "personal_data.json"
with open(file_path, 'r') as file:
    data = json.load(file)

print(data['mortgage_schedule'])