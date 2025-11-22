# functions_example.py
def greet(name="World"):
    return f"Hello, {name}!"

def add(a,b=0):
    return a + b

if __name__ == "__main__":
    print(greet("Alice"))
    print("Add:", add(5,7))
