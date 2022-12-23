class Publisher:
    def __init__(self):
        self.pub = input("Enter name of the publisher : ")
    
    def display(self):
        print(f"Publisher : {self.pub}")

class Book(Publisher):
    def __init__(self):
        super().__init__()
        self.title = input("Enter name of the title : ")
        self.author = input("Enter name of the author : ")

    def display(self):
        super().display()
        print(f'Title : {self.title}')
        print(f'Author : {self.author}')

class Python(Book):
    def __init__(self):
        super().__init__()
        self.price = int(input("Enter price of the book : "))
        self.page  = int(input("Enter no of pages : "))

    def display(self):
        super().display()
        print(f'Price : {self.price}')
        print(f'No of pages : {self.page}')

book1 = Python()
book1.display()