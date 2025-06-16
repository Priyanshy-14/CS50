def main():
    greet = input("Greeting: ").strip().lower()
    result = value(greet)
    print(f"${result}")


def value(greeting):
    num = 0
    if "hello" in greeting:
        num =0
    elif greeting.startswith("h"):
        num = 20
    else:
        num = 100

    return num


if __name__ == "__main__":
    main()
