"""
    Write recursive program that display below pattern  

    Input : 879
    
    Output :   24

"""

def Display(Digit,i = 0,Ans = 0):

    if Digit > 0:
        i+=1
        iTemp = Digit % 10
        Ans = Ans + iTemp
        print(Ans)
        Digit = int(Digit / 10)
        return Display(Digit,i,Ans)
    return Ans
        # if Digit == 0:
            # return(Ans)
   

def main():
    print("Demonstration of Recurssive problem")
    iRet = 0
    Value = int(input("Enter a number : "))
    iRet = Display(Value)
    print("Result is : ",iRet)

if __name__ == "__main__":
    main()


