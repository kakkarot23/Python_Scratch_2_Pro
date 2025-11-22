# threading_example.py
import threading, time

def worker(id, delay):
    print(f"Worker {id} starting")
    time.sleep(delay)
    print(f"Worker {id} done")

if __name__ == "__main__":
    t1 = threading.Thread(target=worker, args=(1,2))
    t2 = threading.Thread(target=worker, args=(2,1))
    t1.start(); t2.start()
    t1.join(); t2.join()
    print("All done")
