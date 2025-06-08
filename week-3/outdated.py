months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Date: ").strip()
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

        elif "," in date:
            month , x = date.split(" ", 1)
            month = month.title()
            month = months.index(month) +1
            x= x.replace(" ", "")
            day, year = x.split(",")
            day = int(day)
            year = int(year)

        if 1<=month<=12 and 1<=day<=31:
            print(f"{year:04}-{month:02}-{day:02}")
            break

    except (ValueError, IndexError):
        continue
