"""
write a program which accept N number from user and return addition of all elements from the list.

Input : 13  5   45  7   4   56

Output : 130

"""
def Add(Length,Arr):
    i = 0
    Ans = 0
    for i in range(Length):
        Ans = Ans + Arr[i]
    return Ans
        


def main():
    Arr = list()

    print("Enter number of elements ")
    No1 = int(input())

    print("Enter the elements : ")
    for i in range(No1):
        Value = int(input())
        Arr.append(Value)

    iRet = Add(No1,Arr)
    print("Addition of the given elements is : ",iRet)

    

if __name__ == "__main__":
    main()