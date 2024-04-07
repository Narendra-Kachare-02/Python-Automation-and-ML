"""
write a program which contain one lambda function which accept one parameter and return of power two

Input : 4
Output : 16

Input : 6
Output : 64

"""

# def Square(No):
#     return No*No
Square = lambda No : No*No

def main():
    iRet = 0

    print("Enter the number : ")
    Value = int(input())

    iRet = Square(Value)
    print("Output is : %d" %iRet)

if __name__ == "__main__":
    main()