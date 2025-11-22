# dict_examples.py
d = {"name": "Alice", "age": 25}
print("Name:", d.get("name"))
d["city"] = "Mumbai"
print("Keys:", list(d.keys()))
print("Values:", list(d.values()))
for k,v in d.items():
    print(k, "->", v)
