"""
write a program which accept N number from user and return Maximum number from that list

Input : 13  5   45  7   4   56

Output : 56

"""
def Maximum(Length,ptr):
    No = 0
    for i in range(Length):
        if(ptr[i] > No):
            No = ptr[i]
    return No
        
        


def main():
    Arr = list()

    print("Enter number of elements ")
    No1 = int(input())

    print("Enter the elements : ")
    for i in range(No1):
        Value = int(input())
        Arr.append(Value)

    iRet = Maximum(No1,Arr)
    print("Maximum number of the given elements is : ",iRet)

    

if __name__ == "__main__":
    main()