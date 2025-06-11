names = []

while True:
    try:
        word = input()
        names.append(word)
    except (EOFError, KeyboardInterrupt)  :
        print()
        break

def greet(names):
    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif len(names) == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    else:
        print(f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}")

greet(names)
