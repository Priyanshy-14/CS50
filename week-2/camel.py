def main():
    camel = input("camelCase:")
    snakify(camel)

def snakify(name):
    snake = ""
    for i in name:
        if i.isupper():
            snake += "_" + i.lower()
        else:
            snake += i

    print(f"snake_case:{snake}")


main()
