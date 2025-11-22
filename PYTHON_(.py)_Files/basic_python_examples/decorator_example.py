# decorator_example.py
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Elapsed: {end-start:.6f}s")
        return result
    return wrapper

@timer
def compute(n):
    s = 0
    for i in range(n):
        s += i
    return s

if __name__ == "__main__":
    print(compute(100000))
