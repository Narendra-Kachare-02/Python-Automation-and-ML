# write a program which display 10 even numbers on screen


def Display(Name):
     
    iCnt = 0
    for i in Name:
        iCnt = iCnt+1

    return iCnt     #direct enter marle tr loop madhe jaty (Level 2 la). Indentation lavel 1 la ghyayche

def main():
    
    print("Enter Name")
    Name = str(input())

    iRet = Display(Name)
    print("Length of the",Name,"is",iRet)

if __name__ == "__main__":
    main()