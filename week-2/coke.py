def main():
    amt = 50
    paid = 0
    while True:
        print(f"Amount Due: {amt-paid}")
        if paid < 50:
            x = int(input("Insert Coin: "))
            if x in [25, 10, 5]:
                paid += x
            if paid>= amt:
                print(f"Change Owed: {paid-amt}")
                break
main()
