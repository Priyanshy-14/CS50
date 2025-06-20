import re

password = input("Enter your password: ")
pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+=<>?]).{8,}$"
match = re.match(pattern, password)
if match:
    print("Strong Password!")
else:
    print("Password not strong enough!")
