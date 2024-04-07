"""
write a program which contain one lambda function which accept two parameter and return its multiplication
Input : 4 3
Output : 12

Input : 6 3
Output : 18

"""

# def Square(No):
#     return No*No
Square = lambda No1,No2 : No1*No2

def main():
    iRet = 0

    try:
        print("Enter first number : ")
        Value1 = int(input())

        print("Enter second number : ")
        Value2 = int(input())
        iRet = Square(Value1,Value2)
    except ValueError as vobj:
        print("Error is : %s"%vobj)
        return
    except Exception as E:
        print("Error is : ",E)
        return

    print("Output is : %d" %iRet)

if __name__ == "__main__":
    main()