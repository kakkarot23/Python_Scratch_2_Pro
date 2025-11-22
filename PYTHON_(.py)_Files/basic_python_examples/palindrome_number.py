# palindrome_number.py
n = int(input("Enter an integer: "))
original = str(n)
rev = original[::-1]
print(f"Reversed: {rev}")
print("Is palindrome:", original == rev)
