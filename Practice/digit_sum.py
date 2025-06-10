def add(num):
    if len(num) == 0: 
        return 0
    else:
        return int(num[0]) + add(num[1:])  

n = input("Number: ")
total = add(n)
print(total)
