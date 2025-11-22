# list_comprehension.py
nums = [x*x for x in range(1,11)]
evens = [x for x in range(1,21) if x%2==0]
pairs = [(x,y) for x in range(1,4) for y in range(1,4)]
print("Squares:", nums)
print("Evens:", evens)
print("Pairs:", pairs)
