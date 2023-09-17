import json

# Reading data from JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Adding a new user (always hash passwords in a real-world scenario!)
data['users'].append({
    'username': 'Alice',
    'password': 'password123'
})

# Writing data back to the JSON file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
