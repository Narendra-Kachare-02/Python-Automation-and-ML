"""
3. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 
70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers.

Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70] 
List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 6538752000

"""
from functools import reduce

Max = lambda No : (No >= 70) and (No<= 90)
Increment = lambda No : No+10
Multiplication = lambda a,b : a*b
    
        




def main():
    
    Arr = []

    print("Enter the number of elements : ")
    Length = int(input())
    for No in range(Length):
        Value = int(input())
        Arr.append(Value)

    R1 = list(filter(Max,Arr))
    print(R1)

    R2 = list(map(Increment,R1))
    print(R2)

    try :
        R3 = reduce(Multiplication,R2)
        print(R3)
    except TypeError as tobj:
        print("Error is : ",tobj)
        return
    except Exception:
        return





if __name__ == "__main__":
    main()