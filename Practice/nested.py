nested = [1, 2, [2, 3], [7, 8, 9], 10]
flat=[]
for i in nested:
    if isinstance(i, list):
        for j in i:
            flat.append(j)
    else:
        flat.append(i)

print("List: ", flat)

