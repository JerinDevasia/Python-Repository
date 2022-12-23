class Time:
    def __init__(self):
        self.__h = int(input("Enter hours : "))
        self.__m = int(input("Enter minutes : "))
        self.__s = int(input("Enter seconds : "))
        if(self.__s > 59):
            self.__s = self.__s - 60
            self.__m += 1
        
        if(self.__m > 59):
            self.__m = self.__m - 60
            self.__h += 1

    def __add__(self,other):
        nt_h = self.__h + other.__h
        nt_m = self.__m + other.__m
        nt_s = self.__s + other.__s

        if(nt_s > 59):
            nt_s = nt_s - 60
            nt_m += 1
        
        if(nt_m > 59):
            nt_m = nt_m - 60
            nt_h += 1

        return(nt_h,nt_m,nt_s)

ob1 = Time()
ob2 = Time()

ob3 = ob1 + ob2
print(f"Hour : {ob3[0]}")
print(f"Minute : {ob3[1]}")
print(f"Second : {ob3[2]}")