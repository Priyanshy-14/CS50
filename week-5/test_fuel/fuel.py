def main():
        div = input("Fraction: ")
        percent = convert(div)
        output = gauge(int(percent))
        print(output)



def convert(fraction):
    x, y = fraction.split("/")
    x=int(x)
    y= int(y)
    if y == 0:
        raise ZeroDivisionError
    
    if x>y:
        raise ValueError

    percent = (int(x)*100)/int(y)
    return percent


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
         return f"{percentage}%"

if __name__ == "__main__":
    main()
