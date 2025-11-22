# fibonacci.py
def fib(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

if __name__ == "__main__":
    n = int(input("How many Fibonacci terms? "))
    print(fib(n))
