def Factorial(No):
    Ans = 1
    for i in range(1,(No+1),1):
        Ans = i * Ans
    return Ans

def main():
    print("Enter the number")
    Value = int(input())

    iRet = Factorial(Value)
    print("Input :",Value,"\n""Output :",iRet)

if __name__ == "__main__":
    main()