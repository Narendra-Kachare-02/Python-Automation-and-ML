"""
Input : 5187934

Output : 37

"""
def AddDigit(No):
    
    iAns = 0
    while(No != 0):
        
        iDigit = No % 10
        iAns = iAns + iDigit
        No = int(No/10)

    return iAns


def main():
    print("Enter the number")
    Value = int(input())

    Ret = AddDigit(Value)
    print("Addition of Each digit is",Ret)

if __name__ == "__main__":
    main()