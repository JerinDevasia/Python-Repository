sentence = "Apple Apple Mango Grape Mango Orange Grape Grape"

l1 = sentence.split(" ")
l2 = []
for x in l1:
    if x not in l2:
        l2.append(x)
for x in range(0, len(l2)):
    print("Frequency of ", l2[x] , " is : ", l1.count(l2[x]))
