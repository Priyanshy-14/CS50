import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r"(?P<grp1>https?\://)(?:www\.)?(?P<grp2>youtube)\.com/embed(?P<vdoUrl>/([a-zA-Z0-9]+))"
    match = re.search(pattern, s)
    if match:
        if s.startswith("<iframe "):
            url = match.group("vdoUrl")
            return f"https://youtu.be{url}"
    else:
        return None
if __name__ == "__main__":
    main()
