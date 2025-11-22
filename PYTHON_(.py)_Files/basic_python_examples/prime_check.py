# prime_check.py
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

if __name__ == "__main__":
    x = int(input("Enter a number: "))
    print(f"{x} is prime: {is_prime(x)}")
