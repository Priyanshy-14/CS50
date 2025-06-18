import sys

def main():

    if len(sys.argv) == 1:
        sys.exit("Too few command line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    if len(sys.argv) == 2:
        Arg = sys.argv[1]
        print(count_line(Arg))

def count_line(filename):
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(filename, "r") as file:
            count = 0
            for line in file:
                if line.lstrip().startswith("#"):
                    continue
                elif line.strip() == "":
                    continue
                else:
                    count+=1
                    continue
            return count
    except FileNotFoundError:
        sys.exit("File does not exist")




if __name__ == "__main__":
    main()
