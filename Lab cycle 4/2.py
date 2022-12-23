class Bank:
    def __init__(self,ac_no,name,ac_type,bal):
        self.__ac_no = ac_no
        self.__name = name
        self.__ac_type = ac_type
        self.__bal = bal

    def deposit(self,amt):
        self.__bal += amt
        print("Deposited Successfully")

    def withdraw(self,amt):
        if(amt > self.__bal):
            print("Cannot withdraw that amount")
        else:
            self.__bal -= amt
            print("Amount withdrawn successfully")
    
    def display(self):
        print(f'Balance : {self.__bal}')


name = input("Enter name : ")
id = int(input("Enter account number : "))
ac_type = input("Enter account type : ")
bal = int(input("Enter balance : "))

ob1 = Bank(id,name,ac_type,bal)
ch = 0
while(ch != 4):
    print("\n1.Deposit \n2.Withdraw \n3.Display \n4.Exit")
    ch = int(input("Enter your choice : "))

    if(ch == 1):
        amt = int(input("Enter amount to deposit : "))
        ob1.deposit(amt)
    elif(ch == 2):
        amt = int(input("Enter amount to withdraw : "))
        ob1.withdraw(amt)
    elif(ch == 3):
        ob1.display()
    else:
        print("Exiting")