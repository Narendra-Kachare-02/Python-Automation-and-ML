def Factorial(No):
    Ans = 0
    for i in range(1,int((No/2)+1)):
        if(No % i == 0):
            Ans = i + Ans
    return Ans

def main():
    print("Enter the number")
    Value = int(input())

    iRet = Factorial(Value)
    print("Input :",Value,"\n""Output :",iRet)

if __name__ == "__main__":
    main()
