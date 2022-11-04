start = int(input("Enter current year : "))
end = int(input("Enter final year : "))

for year in range(start,end):
    if (year%4==0) and (year%100!=0):
        print(year)
