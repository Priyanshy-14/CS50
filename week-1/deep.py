'''METHOD 01
def main():
    ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything?").strip().lower()
    if ans == "forty-two" or ans == "forty two" or ans == "42":
        print("Yes")
    else:
        print("No")
main()'''


# Method 02
ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything?").strip().lower()
match ans:
    case "forty-two" | "forty two" | "42":
        print("yes")
    case _:
        print("no")
