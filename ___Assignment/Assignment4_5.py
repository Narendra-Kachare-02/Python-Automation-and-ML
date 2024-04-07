"""
3. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
List contains the numbers which are accepted from user. Filter should filter out all prime numbers
Map function will multiply each number by 2
Reduce will return Maximum number from that number.

Input List = [2, 70, 11, 10, 17, 23, 31, 77] 

List after filter = [2, 11, 17, 23, 31]

List after map = [4, 22, 34, 46, 62]

Output of reduce = 62

Without using inbuilt module
"""

# filter(CheckPrime,Arr)
def filterX(CheckPrime,Arr):
    Result = []
    for No in Arr:
        if(CheckPrime(No) == True):
            Result.append(No)
    return Result
    
# map(Increment,R1)
def mapX(Increment,R1):
    Result = []
    for No in R1:
        iRet = Increment(No)
        Result.append(iRet)
    return Result
        

# reduce(MaxN,R2)
def reduceX(MaxN,R2):
    a = 0
    for No in R2:
        a = MaxN(a,No)
    return a


def CheckPrime(No):
    if No < 0:
        print("please Enter positive number")
        return
    if No == 1:
        return False
    elif No == 2 or No == 3:
        return True
    else:
        for i in range(2,(int(No/2)+1)):
            if int(No % i) == 0:
                break
        if i == int(No/2):
            return True
        else:
            return False

def Increment(No):
    return No*2

def MaxN(a,b):
    if a > b:
        return a
    else:
        return b



def main():
    Arr = []
    print("Enter the number of elements : ")
    Length = int(input())
    for No in range(Length):
        Value = int(input())
        Arr.append(Value)
    
    print(Arr)
    R1 = list(filterX(CheckPrime,Arr))
    print(R1)

    R2 = list(mapX(Increment,R1))
    print(R2)

    R3 = reduceX(MaxN,R2)
    print(R3)

if __name__ == "__main__":
    main()