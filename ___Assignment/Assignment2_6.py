"""
Input : 5

Output :
            *   *   *   *   *
            *   *   *   *   
            *   *   *   
            *   *   
            *   


"""

def Display(No):
    
    for i in range(No,0,-1):
        for j in range(1,No+1,1):
            if(i >= j):
                print("*",end="\t" )
            
        print("\n\n")

def main():
    print("Enter the number ")
    Value = int(input())

    Display(Value)


if __name__ == "__main__":
    main()


    


    