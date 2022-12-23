class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def area(self):
        a = self.l * self.b
        return a

    def perimeter(self):
        p = 2 * (self.l + self.b)
        return p

ob1 = Rectangle(2,3)
ob2 = Rectangle(3,4)

area1 = ob1.area()
peri1 = ob1.perimeter()

print("1st object")
print(f'Area : {area1} Perimeter : {peri1} ')

area2 = ob2.area()
peri2 = ob2.perimeter()

print("\n2nd object")
print(f'Area : {area2} Perimeter : {peri2} ')

if area1 > area2:
    print("\nArea of 1st object is greater")
else:
    print("\nArea of 2nd object is greater")