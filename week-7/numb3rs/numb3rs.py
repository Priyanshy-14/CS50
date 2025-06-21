import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.fullmatch(pattern, ip)
    if match:
        for n in match.groups():
            if not (0 <= int(n) <= 255):
                return False
        return True
    return False

if __name__ == "__main__":
    main()
