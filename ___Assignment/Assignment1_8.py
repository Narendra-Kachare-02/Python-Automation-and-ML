# accept  a number from user and and print that number times * on scrren.

def Display(iNo):

    for i in range(0,iNo,1):
        print('* ')

def DisplayX(iNo):
    print("New Method")
    print("* " * iNo)

def main():

    iValue = 0

    print("Enter the number")
    iValue = int(input())

    Display(iValue)

    DisplayX(iValue)
    
    
    
if __name__ == "__main__":
    main()