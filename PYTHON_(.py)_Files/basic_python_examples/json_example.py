# json_example.py
import json
data = {"name":"Alice","age":30,"skills":["python","sql"]}
s = json.dumps(data)
print("JSON string:", s)
obj = json.loads(s)
print("Loaded:", obj)
