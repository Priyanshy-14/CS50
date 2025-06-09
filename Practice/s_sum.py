'''1. Write a program to accept a positive integer n and print the sum of the following series: 1
+ 11 + 111 + ... (n terms)'''

series = []
x = int(input("Enter the value of n: "))
a = ""

for i in range(x):
    a+="1"
    series.append(int(a))

total = 0
for num in series:
    total += num
print("Series: 1+ 11 + 111 + ... (n terms)")
print("sum of series:", total)

    
