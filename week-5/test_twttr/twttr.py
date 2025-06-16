def main():
    string = input("Input:")
    output = shorten(string)
    print(f"Output:{output}")


def shorten(word):
    vowels = "AEIOUaeiou"
    output = "".join(i for i in word if i not in vowels)
    return output


if __name__ == "__main__":
    main()

