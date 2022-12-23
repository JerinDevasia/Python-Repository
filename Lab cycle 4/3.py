class Rectangle:
    def __init__(self):
        self.__len = int(input("Enter length : "))
        self.__width = int(input("Enter width : "))
        self.area = self.__len * self.__width

    def __lt__(self,other):
        if(self.area < other.area):
            return True
        else:
            return False
    
ob1 = Rectangle()
ob2 = Rectangle()

if(ob1 < ob2):
    print("obt2 is greater")
else:
    print("ob1 is greater")