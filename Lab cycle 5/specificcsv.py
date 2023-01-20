import csv

with open("letter_frequency.csv","r") as fle:

    lst = csv.reader(fle)
    col1 = col2 = col3 = []
    for i in lst:
        col1.append(i[0])
        col2.append(i[1])
        col3.append(i[2])
    print(f"Column 1 : {col1} \n\n")
    print(f"Column 2 : {col2} \n\n") 
    print(f"Column 3 : {col3} \n\n")