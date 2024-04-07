"""
    Write recursive program that display below pattern  

    Input : 5
    
    Output :   *   *   *   *   *

"""
i = 1
def Display(no):
    global i
    if i <= no:
        print("*",end="\t")
        i+=1
        Display(no)


def main():
    print("Demonstration of Recurssive problem")
    Value = int(input("Enter a number : "))
    Display(Value)

if __name__ == "__main__":
    main()


