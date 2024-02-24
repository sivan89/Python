import json
import yaml
json_string='{"name": {"first": "John", "last": "Doe"}, "address": {"street": "123 Main St", "city": "Anytown", "state": "CA", "zipcode": "12345"}, "email": "john.doe@example.com", "age": 32}'
print("The JSON string is:")
print(json_string)

python_dict=json.loads(json_string)
ymal_string=yaml.dump(python_dict)
print("The YAML string is:")
print(ymal_string)