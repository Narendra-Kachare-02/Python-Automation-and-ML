# accept  a number from user and and check whether that number is positive Negative or zero

def Check(iNo):
    if(iNo >= 0):
        if(iNo == 0):
            print("Zero")
        else:
            print("Positive Number")
    
    else:
        print("Negative Number")

def CheckX(iNo):
    if(iNo > 0):
        print("Positive Number")
    elif(iNo == 0):
        print("Zero")
    else:
        print("Negative Number")

    

    

def main():

    iValue = 0

    print("Enter the number")
    iValue = int(input())

    Check(iValue)
    CheckX(iValue)
    
    
if __name__ == "__main__":
    main()