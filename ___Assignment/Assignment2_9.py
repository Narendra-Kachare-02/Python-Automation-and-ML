"""
Input : 5187934

Output : 7

"""

def CountDigit(No):

    iCount = 0
    while(No != 0):

        No = int(No / 10)
        iCount = iCount + 1

    return iCount

    


def main():
    print("Enter the number ")
    Value = int(input())

    print("Input :",Value,"\n")

    iRet = CountDigit(Value)
    print("Output :",iRet)


if __name__ == "__main__":
    main()


    


    