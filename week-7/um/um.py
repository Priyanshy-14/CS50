import re

def main():
    print(count(input("Text: ").strip()))

def count(s):
    pattern = r"(\bum\b)"
    count =0
    for match in re.finditer(pattern, s, flags = re.IGNORECASE):
        count+=1
    return count

if __name__ == "__main__":
    main()