import validators

def main():
    e = input("What's your email address?")
    if validators.email(e) == True:
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
