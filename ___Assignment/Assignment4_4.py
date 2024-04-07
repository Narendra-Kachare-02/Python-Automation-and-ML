"""
3. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
List contains the numbers which are accepted from user. Filter should filter out all such numbers which are Even
Map function will calculate its square.
Reduce will return addition of all that number.

Input List = [11,12,13,14,15] 
List after filter = [12, 14]
List after map = [144, 196]     
Output of reduce = 340

"""
from functools import reduce

Even = lambda No : (No % 2 == 0)
Square = lambda No : No*No
Add = lambda a,b : a+b
    




def main():
    
    Arr = []

    print("Enter the number of elements : ")
    Length = int(input())
    for No in range(Length):
        Value = int(input())
        Arr.append(Value)

    R1 = list(filter(Even,Arr))
    print(R1)

    R2 = list(map(Square,R1))
    print(R2)

    try :
        R3 = reduce(Add,R2)
        print(R3)
    except TypeError as tobj:
        print("Error is : ",tobj)
        return
    except Exception:
        return


    # print(reduce(Add,map(Square,filter(Even,Arr))))
    # print(reduce(lambda a,b : a+b,map(lambda No : No*No,filter(lambda No : (No % 2 == 0),Arr))))





if __name__ == "__main__":
    main()