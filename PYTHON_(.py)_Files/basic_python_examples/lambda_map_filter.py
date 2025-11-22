# lambda_map_filter.py
nums = list(range(1,11))
squares = list(map(lambda x: x*x, nums))
evens = list(filter(lambda x: x%2==0, nums))
print("Nums:", nums)
print("Squares:", squares)
print("Evens:", evens)
