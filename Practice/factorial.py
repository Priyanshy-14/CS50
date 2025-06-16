def fact(num):

    for i in range(1, num+1):
        factorial = num*i
        return factorial
def get():
    x = int(input("Enter a number:"))
    res = fact(x)
    print(f"Factorial of {x} is {res:.2f}")


get()
