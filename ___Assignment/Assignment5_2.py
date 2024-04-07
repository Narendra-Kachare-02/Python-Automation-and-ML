"""
2. Write a program which contains one class named as Circle.
Circle class contains three instance variables as Radius,Area, Circumference.
That class contains one class variable as PI which is initialise to 3.14. Inside init method initialise all instance variables to 0.0.
There are three instance methods inside class as Accept(), CalculateArea(), CalculateCircumference(), Display().

Accept method will accept value of Radius from user.
CalculateArea() method will calculate area of circle and store it into instance variable Area.
CalculateCircumference() method will calculate circumference of circle and store it into instance variable Circumference.
And Display() method will display value of all the instance variables as Radius , Area,
Circumference.
After designing the above class call all instance methods by creating multiple objects

"""
class Circle:

    PI = float(22/7)
    
    PI = float(PI)
    
    def __init__(self):
        self.Radius = 0.0
        self.Radius = float(self.Radius)

        self.Area = 0.0
        self.Area = float(self.Area)

        self.Circumference = 0.0
        self.Circumference = float(self.Circumference)
    
    def Accept(self):
        try:
            self.Radius = float(input("Enter radius of a circle : \n"))
        except ValueError as vobj:
            print("Error is : %s"%vobj)
            return
        except Exception as E:
            print("Error is : ",E)
            return
    
    def CalculateArea(self):
        self.Area = self.PI *self.Radius*self.Radius
        return self.Area
    
    def CalculateCircumference(self):
        self.Circumference = 2 * self.PI * self.Radius
        return self.Circumference
    
    def Display(self):
        iRet = self.CalculateArea()
        print("Area of a circle : ",iRet)

        iRet = self.CalculateCircumference()
        print("Perimeter of a circle is : %s\n"%iRet)



def main():
    obj1 = Circle()
    obj1.Accept()
    obj1.Display()

    obj2 = Circle()
    obj2.Accept()
    obj2.Display()


    

if __name__ == "__main__":
    main()