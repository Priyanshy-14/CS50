list = []
n = int(input("Size of list: "))
for _ in range(n):
    num = int(input("Number: "))
    list.append(num)
if n<2:
    print("List should have atleast 2 elements!")
    
largest = max(list)
list.remove(largest)
print("Second Largest in the list is: ", max(list))
