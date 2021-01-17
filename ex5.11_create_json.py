import json

data = {
    'name': 'Tom',
    'age': 34,
    'income':{
        'salary': 90000,
        'bonus': 20000
    }
}

#записали?
'''with open('my_json.json', 'w') as f:
    json.dump(data, f)'''

with open('my_json.json', 'r') as f:
    new_data = json.load(f)

print(new_data['name'])