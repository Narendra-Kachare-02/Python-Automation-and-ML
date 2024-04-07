"""
Input : 5

Output :
            1
            1   2
            1   2   3
            1   2   3   4
            1   2   3   4   5   


"""

def Display(No):

    print("Output :")
    
    for i in range(1,No+1,1):
        for j in range(1,No+1,1):
            if( i >= j):
                print("\t",j,end="" )
        
        print("\n\n")

def main():
    print("Enter the number ")
    Value = int(input())

    print("Input :",Value,"\n")

    Display(Value)


if __name__ == "__main__":
    main()


    


    