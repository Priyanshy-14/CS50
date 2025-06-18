import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command line arguments")

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    if not file1.endswith(".csv") or not file2.endswith(".csv"):
        sys.exit("Not a CSV file")

    new_file(file1, file2)

def new_file(old, new):
    try:
        with open(old, "r") as file:
            reader = csv.DictReader(file)
            data = []

            for row in reader:
                try:
                    last, first = row["name"].split(",")
                    data.append({ "first": first.strip(), "last": last.strip(), "house": row["house"].strip() })

                except ValueError:
                    continue 

        with open(new, "w", ) as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in data:
                writer.writerow(row)

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
