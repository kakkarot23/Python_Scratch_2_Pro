# class_example.py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

if __name__ == "__main__":
    p = Person("Jay", 30)
    print(p.greet())
