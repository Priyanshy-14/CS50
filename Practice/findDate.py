'''Take a text input (e.g., The meeting is on 13/06/2025 and the next one is on 14-06-2025).
•	Use regex to find all dates in different formats
•	Convert them to a unified format: YYYY-MM-DD
•	Raise exception if no valid date is found
'''
import re

text = input("Enter Text: ").strip()

pattern = r"\b(0[1-9]|[12][0-9]|3[01])[-/](0[1-9]|1[0-2])[-/](\d{4})\b"

matches = list(re.finditer(pattern, text))

found = False

for match in matches:
    day, month, year = match.groups()
    formatted = f"{year}-{month}-{day}"
    print(formatted)
    found = True

if not found:
    raise Exception("No valid dates found.")

