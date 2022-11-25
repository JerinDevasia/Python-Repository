def longestword(l):
    count = 0
    for i in l:
        if len(i) > count:
            count = len(i)
    return count

l = list(input("Enter words : ").split(" "))
print("Length of longest word : ",longestword(l))
    
