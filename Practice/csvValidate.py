import re

csv_data = """
Khushi,kussi@example.com,9876543210
Priyanshy,priii.doe@,987654321
Smith,smith@gmail.com,9123456789
Bad Line,missingemail.com
Empty Line,,,
"""

email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
phone_pattern = r"^[6-9]\d{9}$"

print("Valid Entries:")

lines = csv_data.strip().split('\n')
line_number = 1

for line in lines:
    parts = line.split(",")

    if len(parts) < 3:
        print(f"Line {line_number}: Invalid — missing fields")
    else:
        name = parts[0].strip()
        email = parts[1].strip()
        phone = parts[2].strip()

        if not re.fullmatch(email_pattern, email):
            print(f"Line {line_number}: Invalid email — '{email}'")
        elif not re.fullmatch(phone_pattern, phone):
            print(f"Line {line_number}: Invalid phone — '{phone}'")
        else:
            print(f"{line_number}. {name} - {email}, {phone}")
    
    line_number += 1
