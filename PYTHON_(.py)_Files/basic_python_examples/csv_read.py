# csv_read.py
import csv
fname = "sample.csv"
# create sample csv
with open(fname, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["name","age"])
    writer.writerow(["Alice",30])
    writer.writerow(["Bob",25])
print("Created sample.csv")

# read it
with open(fname, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
