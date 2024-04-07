def CheckPrime(No):
    
    if(No == 2 or No == 3 or No == 5):
        return True
    for i in range(2,int(No/2)+1):
        if(No % i == 0):
            break

        return True
        


def main():
    print("Enter the number")
    Value = int(input())

    Ret = CheckPrime(Value)
    if(Ret == True):
        print("It is Prime Number")
    else:
        print("It is not Prime Number ")


if __name__ == "__main__":
    main()