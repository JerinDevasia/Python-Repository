str1 = "abc"
str2 = "xyz"

x = str1[1]
y = str2[1]
str1 = str1[0] + y + str1[2:]
str2 = str2[0] + x + str2[2:]

str3 = str1 + ' ' + str2
print(str3)