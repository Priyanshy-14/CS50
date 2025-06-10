string = input("Enter a string: ").strip().lower()
vowels = ["a", "e", "i", "o", "u"]

print("Vowels:")
for ch in set(string):
    if ch in vowels:
        print(ch, ":", string.count(ch))

print("Consonants:")
for ch in set(string):
    if ch.isalpha() and ch not in vowels:
        print(ch, ":", string.count(ch))
