def fnstring(str):
    if str[-3:] == "ing":
        newstr = str+ "ly"
        return newstr
    else:
        str = str + "ing"
        return str

str = input("Enter a string : ")
print(fnstring(str))