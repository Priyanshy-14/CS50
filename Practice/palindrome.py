def is_palindrome(word):
    x = word
    y = "".join(reversed(word))
    return x==y
    
def get():
    word = input("Enter a word:").strip()
    res = is_palindrome(word)
    if res==True:
        print(f"yes, {word} is a palindrome word!")
    else:
        print(f"No, {word} is not a  palindrome word!")

get()



