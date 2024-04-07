"""
    Write recursive program that display below pattern  

    Input : 5
    
    Output : 120

"""

def Display(Digit):
    if Digit == 0 or Digit == 1:
        return 1
    else:
        return Digit * Display(Digit-1)
    

def main():
    print("Demonstration of Recurssive problem")
    iRet = 0
    Value = int(input("Enter a number : "))
    iRet = Display(Value)
    print("Result is : ",iRet)

if __name__ == "__main__":
    main()


