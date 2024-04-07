# accept two numbers and return addition of two numbers

def Add(iNo1, iNo2):
    Ans = 0
    Ans = iNo1 + iNo2
    return Ans

    

def main():
    iValue1 = 0
    iValue2 = 0
    
    print("Enter the  first number : ")
    iValue1 = int(input())

    print("Enter the second number")
    iValue2 = int(input())

    iRet = Add(iValue1, iValue2)
    print("Addition will be : ",iRet)
    
if __name__ == "__main__":
    main()