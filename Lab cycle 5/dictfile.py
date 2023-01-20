import csv
my_dict = {'1':"hello",'2':"world",'3':"hi"}

with open('new.csv','w') as f:
    for key in my_dict.keys():
        string = str(key) + "," + str(my_dict[key]) + "\n"
        f.write(string)

with open('new.csv',mode="r") as file:
    csvfile = csv.reader(file)
    for line in csvfile:
        print(line)