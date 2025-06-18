import sys
import csv
from tabulate import tabulate

def main():

    if len(sys.argv) == 1:
        sys.exit("Too few command line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    if len(sys.argv) == 2:
        Arg = sys.argv[1]
        print(show_table(Arg))

def show_table(filename):
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            return tabulate(reader, tablefmt="grid")

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
