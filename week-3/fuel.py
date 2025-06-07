def main():
    while True:

        try:
            div = input("Fraction:")
            x, y = div.split("/")
            x=int(x)
            y= int(y)
            percent = (x*100)/y

            if x>y:
                raise ValueError

            if percent<= 1:
                print("E")
            elif percent >= 99:
                print("F")
            else:
                print(f"{round(percent)}%")

        except ValueError:
            continue
        except ZeroDivisionError:
            continue

        break


main()

