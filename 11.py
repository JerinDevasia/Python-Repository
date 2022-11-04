list=['Robin','Rahul','Roshin','Rijfas','Rifana','Anand']
count = 0
for i in list:
    for j in i:
        if 'a'== j or 'A'==j:
            count = count+1

print(count)
