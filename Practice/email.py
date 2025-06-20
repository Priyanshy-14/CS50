import re

allowed_domains = ["gmail.com", "yahoo.com", "outlook.com"]

emails = [
    "priyanshy@gmail.com",
    "test@outlook.com",
    "user@yahoo.com",
    "abc@unknown.org",
    "invalidemail"
]

for email in emails:
    match = re.match(r"^[\w\.-]+@([\w\.-]+\.\w+)$", email)
    if match:
        domain = match.group(1).lower()
        print( "Domain:", domain)
        if domain not in allowed_domains:
            print(" Error: Domain not allowed -", domain)
    else:
        print(" Invalid email format:", email)

