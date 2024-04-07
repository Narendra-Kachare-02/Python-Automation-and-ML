# Accept number from user and display Even or Odd
def ChkNum(iNo):
    if(iNo % 2 == 0):
        return True
    else:
        return False

def main():
    iValue = 0
    
    print("Enter the number : ")
    iValue = int(input())

    bRet = ChkNum(iValue)

    if(bRet == True):
        print("Even Number")
    else:
        print("Odd Number")


    
if __name__ == "__main__":
    main()