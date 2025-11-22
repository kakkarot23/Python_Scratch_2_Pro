# list_operations.py
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("List:", nums)
print("Sum:", sum(nums))
print("Max:", max(nums) if nums else None)
print("Min:", min(nums) if nums else None)
print("Sorted:", sorted(nums))
