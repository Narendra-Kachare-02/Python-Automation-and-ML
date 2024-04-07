"""
2. Write a program which contains one class named as BankAccount.
BankAccount class contains two instance variables as Name & Amount. 
That class contains one class variable as ROI which is initialise to 10.5.
Inside init method initialise all name and amount variables by accepting the values from user.
There are Four instance methods inside class as Display(), Deposit(), Withdraw(), CalculateIntrest().
Deposit() method will accept the amount from user and add that value in class instance variable Amount.
Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
CalculateIntrest() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI.
And Display() method will display value of all the instance variables as Name and Amount.
After designing the above class call all instance methods by creating multiple objects.

"""
class BankAccount:

    ROI = 10.5
    ROI = float(ROI)

    def __init__(self):
        self.Name = input("Enter your name : ")
        self.Amount = float(input("Enter your Amount : "))
        
    def Display(self):
        print("Your name : ",self.Name)
        print("Account Balance : ",self.Amount)
        Separator = "-"*75
        print(Separator)

    
    def Deposit(self):
        DepositX = float(input("\nEnter Deposit Amount :\n"))
        self.Amount = self.Amount + DepositX
        print("Amount Deposited successfully")
        self.Display()
        

    def Withdraw(self):
        WithdrawX = float(input("Enter Withdraw Amount :\n"))
        self.Amount = self.Amount - WithdrawX
        print("Amount Withdraw successfully")
        if(self.Amount < 0):
            exit()
        self.Display()

    
    def CalculateInterst(self):
        print("Your Balance is : ",self.Amount)
        Interest = float(self.Amount / self.ROI)
        self.Amount = self.Amount + Interest

        print("Intesrest Addded : ",Interest)
        self.Display()
    
        

def main():
    obj1 = BankAccount()
    i = 1
    
    while(True):
        print("Press")
        print("1 : Deposit")
        print("2 : Withdraw")
        print("3 : Exit")
        if(i % 4 == 0):
            obj1.CalculateInterst()
        i+=1
        try:
            Value = int(input("Input : " ))
            if(Value == 1):
                obj1.Deposit()
            elif(Value == 2):
                obj1.Withdraw()
            elif(Value == 3):
                print("Thank you for using BOM")
                break
        except ValueError as vobj:
            print("Error : ",vobj)
        except Exception:
            return
        

        
    


if __name__ == "__main__":
    main()