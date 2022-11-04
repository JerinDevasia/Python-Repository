l1 = ['red','green','orange']
l2 = ['purple','blue','green']
l3 = []

for colors in l1:
    if colors not in l2:
        l3.append(colors)

print(l3)