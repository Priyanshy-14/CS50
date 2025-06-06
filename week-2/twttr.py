def main():
    string = input("Input:")
    for i in string:
        if i in ["a", "e", "i", "o", "u"]:
            string = string.replace(i, "")
    print(f"Output:{string}")

main()
