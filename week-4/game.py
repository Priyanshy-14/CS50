'''Prompts the user for a level n,
. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and n
, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
'''
import random
def main():
    while True:
        try:
            n = int(input("Level: "))
            if n>0:
                break
        except ValueError:
            pass

    num = random.randint(1, n)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <=0:
                continue

            if guess< num:
                print("Too small!")
                continue
            elif guess> num:
                print("Too large!")
                continue
            else:
                print("Just right!")
                break
        except ValueError:
            pass

main()
