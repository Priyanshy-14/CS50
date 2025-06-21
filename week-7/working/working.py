
import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.fullmatch(pattern, s, flags=re.IGNORECASE)
    if not match:
        raise ValueError("Invalid format")

    h1, m1, ampm1, h2, m2, ampm2 = match.group(1), match.group(2), match.group(3).upper(), match.group(4), match.group(5), match.group(6).upper()

    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0

    h1 = int(h1)
    h2 = int(h2)

    # Validate time values
    if not (1 <= h1 <= 12 and 0 <= m1 < 60 and 1 <= h2 <= 12 and 0 <= m2 < 60):
        raise ValueError("Invalid time values")

    time1 = to_24_hour(h1, m1, ampm1)
    time2 = to_24_hour(h2, m2, ampm2)

    return f"{time1} to {time2}"

def to_24_hour(hour, minute, period):
    if period == "AM":
        if hour == 12:
            hour = 0
    elif period == "PM":
        if hour != 12:
            hour += 12
    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
