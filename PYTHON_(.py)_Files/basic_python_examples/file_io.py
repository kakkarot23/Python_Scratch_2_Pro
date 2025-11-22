# file_io.py
fname = "sample.txt"
with open(fname, "w") as f:
    f.write("This is a sample file.\nLine 2.\n")
print(f"Wrote to {fname}")

with open(fname, "r") as f:
    print("Contents:")
    print(f.read())
