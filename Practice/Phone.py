'''2: Phone Number Formatter and Checker Problem:
Write a script to read phone numbers from user input (e.g., 9876543210, +91-98765-43210)
Use regex to detect valid Indian phone number formats, Normalize all numbers to the format +91-XXXXXXXXXX, Raise an exception for invalid length or pattern
'''
import re

ph = input("Enter the phone number:")
pattern = r"^(?:\+91-)?([6-9]\d{9})$"
match = re.match(pattern, ph)
if match:
    number = match.group(1) 
    print(f"+91-{number}")
else:
    print("Invalid phone number")

    
