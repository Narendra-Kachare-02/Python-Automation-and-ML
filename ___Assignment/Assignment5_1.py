"""
Write a program which contains one class named as Demo.
Demo class contains two instance variables as no1, no2.
That class contains one class variable as Value.
There are two instance methods of class as Fun and Gun which displays values of instance variables.

Initialise instance variable in init method by accepting the values from user.

After creating the class create the two objects of Demo class as
Obj1 Demo(11,21)
Obj2 = Demo(51,101)
Now call the instance methods as
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()
"""

class Demo:

    Value = None
    def __init__(self):
        self.No1 = int(input("Enter first number : "))
        self.No2 = int(input("Enter second number : "))

    
    def Fun(self):
        print("Inside Fun")
        print(self.No1)
        print(self.No2)
    
    def Gun(self):
        print("Inside Gun")
        self.Fun()


def main():
    

    obj1 = Demo()
    obj2 = Demo()

    obj1.Fun()
    obj1.Gun()

    obj2.Fun()
    obj2.Gun()

if __name__ == "__main__":
    main()