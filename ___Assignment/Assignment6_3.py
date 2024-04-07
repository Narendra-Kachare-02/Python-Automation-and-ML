"""
3. Write a program which contains one class named as Numbers.
Arithmetic class contains one instance variables as Value.
Inside init method initialise that instance variables to the value which is accepted from user.
There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),
Factors().
ChkPrime() method will returns true if number is prime otherwise return false.
ChkPerfect() method will returns true if number is perfect otherwise return false.
Factors() method will display all factors of instance variable.
SumFactors() method will return addition of all factors. Use this method in any another method as a helper method if required.
After designing the above class call all instance methods by creating multiple objects.

"""
class Arithmetic:
    
    def __init__(self,i):
        self.No = i
    
    def ChkPrime(self):
        iRet = self.SumFactors()
        if(iRet == 1):
            return False
        elif(iRet == 1+self.No):
            return True
        else:
            return False

    def ChkPerfect(self):
        iRet = self.SumFactors()
        
        if(self.No == iRet - self.No):
            return True
        else:
            return False
        
    
    def SumFactors(self):
        Ans = 0
        iRet = self.Factors()
        if (iRet == 1):
            return iRet
        for no in iRet:
            Ans = Ans + no
        return (Ans+self.No)

    
    def Factors(self):
        Result = []
        if(self.No == 1):
            return self.No
        else:
            for i in range(1,int(self.No/2)+1):
                if(self.No % i == 0):
                    Result.append(i)
            return Result
    
    def Display(self):

        iRet = self.Factors()
        print("Factors will be : ",iRet)

        iRet = self.SumFactors()
        print("SumFactors will be : ",iRet)

        iRet = self.ChkPrime()
        if(iRet == True):
            print("It is prime number")
        else:
            print("It is not prime number")

        iRet = self.ChkPerfect()
        if(iRet == True):
            print("It is Perfect number")
        else:
            print("It is not Perfect number")
        print("")



def main():
    Value = int(input("Enter the number : \n"))
    obj1 = Arithmetic(Value)
    obj1.Display()

    Value = int(input("Enter the number : \n"))
    obj2 = Arithmetic(Value)
    obj2.Display()
 




if __name__ == "__main__":
    main()