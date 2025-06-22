from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    birth_date = input("Date of Birth (YYYY-MM-DD): ")
    try:
        birth = date.fromisoformat(birth_date)
    except ValueError:
        sys.exit("Invalid date format")

    today = date.today()
    minutes = calculate_minutes(birth, today)
    words = convert_to_words(minutes)
    print(f"{words} minutes")

def calculate_minutes(birth, today):
    x = today - birth
    return round(x.days * 24 * 60)

def convert_to_words(number):
    return p.number_to_words(number, andword="").capitalize()

if __name__ == "__main__":
    main()
