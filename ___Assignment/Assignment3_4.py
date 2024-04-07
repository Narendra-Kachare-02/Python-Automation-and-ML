"""
write a program which accept N numbers from user and store it into list.
accept one another number from user and return frequency of that number from list.

Number of elements : 7
Input : 13  5   45  7   4   56
Search element : 5

Output : 1

"""
def Frequency(Length,ptr,Search):
    for i in range(Length):
        if(ptr[i] == Search):
            break
        
    return i
        
        


def main():
    Arr = list()

    print("Enter number of elements ")
    No1 = int(input())

    print("Enter the elements : ")
    for i in range(No1):
        Value = int(input())
        Arr.append(Value)

    print("Enter the number you want to search")
    No2 = int(input())

    iRet = Frequency(No1,Arr,No2)
    print("Frequency number of the given elements is : ",iRet)

    

if __name__ == "__main__":
    main()