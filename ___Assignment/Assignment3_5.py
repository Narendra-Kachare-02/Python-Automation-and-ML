"""
5. Write a program which accept N numbers from user and store it into List. 
Return addition of all prime numbers from that List. Main python file accepts N numbers from user and 
pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum.
Name of the function from main python file should be ListPrime().

Number of elements : 7
Input : 13  5   45  7   4   56

Output : 25

"""

import MarvellousNum

def main():
    Arr = list()
    iRet = 0

    print("Enter number of elements ")
    No1 = int(input())

    print("Enter the elements : ")
    for i in range(No1):
        Value = int(input())
        Arr.append(Value)

    iRet = MarvellousNum.ChkPrime(Arr)
    print("Addition of prime number is : ",iRet)

    

if __name__ == "__main__":
    main()