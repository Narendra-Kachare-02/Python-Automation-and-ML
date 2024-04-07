def Display(iRow,iCol):
    i = 0
    j = 0
    for i in range(0,iRow,1):
        for j in range(0,iCol,1):
            print("*  ",end=" ")
        
        print("\n")
    

def main():
    print("Enter the number of Rows")
    No1 = int(input())

    print("Enter the number of Column")
    No2 = int(input())

    Display(No1,No2)

if __name__ == "__main__":
    main()