def strcount(str):
    l = []
    for i in str:
        if i not in l:
            l.append(i)

    for x in range(0,len(l)):
        print("Frequency of ", l[x]," is" , str.count(l[x]))

str = input("Enter a word : ")
strcount(str)