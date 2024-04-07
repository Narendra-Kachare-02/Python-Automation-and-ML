"""
    Write recursive program that display below pattern  

    Input : 5
    
    Output :   1   2   3   4   5

"""
i = 0
def Display(no):
    global i
    if i < no:
        
        print(no - i,end="\t")
        i+=1
        Display(no)


def main():
    print("Demonstration of Recurssive problem")
    Value = int(input("Enter a number : "))
    Display(Value)

if __name__ == "__main__":
    main()


