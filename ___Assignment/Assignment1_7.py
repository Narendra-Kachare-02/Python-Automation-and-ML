# accept  a number from user and and check whether that number is divisible by 5 or not.

def Check(iNo):

    if(iNo % 5 == 0):
        return True
    else:
        return False

def main():

    iValue = 0

    print("Enter the number")
    iValue = int(input())

    bRet = Check(iValue)
    if(bRet == True):
        print("True")
    else:
        print("False")
    
    
if __name__ == "__main__":
    main()