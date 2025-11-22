# regex_example.py
import re
s = input("Enter text: ")
emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", s)
print("Emails found:", emails)
