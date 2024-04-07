"""
3. Write a program which contains one class named as Arithmetic.
Arithmetic class contains three instance variables as Value1,Value2. 
Inside init method initialise all instance variables to 0.
There are three instance methods inside class as Accept(), Addition(), Subtraction(), Multiplication(), Division().
Accept method will accept value of Value1 and Value2 from user.
Addition() method will perform addition of Value1,Value2 and return result.
Subtraction() method will perform subtraction of Value1,Value2 and return result.
Multiplication() method will perform multiplication of Value1,Value2 and return result.
Division() method will perform division of Value1,Value2 and return result.
After designing the above class call all instance methods by creating multiple objects

"""

class Arithmetic:
    def __init__(self):
        self.Value1 = 0.0
        self.Value2 = 0.0

    def Accept(self):
        try:
            self.Value1 = float(input("\nEnter first number : \n"))
            self.Value2 = float(input("Enter second number : \n"))
        except ValueError as vobj:
            print("Error is : ",vobj)
        except Exception as E:
            print("Error is ",E)


    def Addition(self):
        return (self.Value1 + self.Value2)

    def Substraction(self):
        return (self.Value1-self.Value2)

    def Multiplication(self):
        return (self.Value1*self.Value2)

    def Division(self):
        try:
            Ans = 0.0
            Ans = self.Value1/self.Value2
            return Ans
        except ZeroDivisionError as zobj:
            print("\nZeroDivisionError : ",zobj)
            
        
        

    def Display(self):
        iRet = self.Addition()
        print("Addition is : ",iRet)

        iRet = self.Substraction()
        print("Substraction is : ",iRet)

        iRet = self.Multiplication()
        print("Multiplication is : ",iRet)

        iRet = self.Division()
        print("Division is : ",iRet)
        Separator = "-"*62
        print(Separator)




def main():
    obj1 = Arithmetic()
    obj1.Accept()
    obj1.Display()

    obj2 = Arithmetic()
    obj2.Accept()
    obj2.Display()

    obj3 = Arithmetic()
    obj3.Accept()
    obj3.Display()



if __name__ == "__main__":
    main()