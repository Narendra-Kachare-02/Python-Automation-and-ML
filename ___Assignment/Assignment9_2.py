"""
    write a program which accepts file name from user and open that file and display the contents of that file on screen

    Input : Demo.txt
    Check whether Demo.txt exists or not.

"""
import os

def main():

    # Accept file
    File_name = input("Enter file name : \n")
    
    # Check file exists or not.
    if os.path.exists(File_name):
        fobj = open(File_name,"r")        
        if fobj:
            Data = fobj.read(File_name)
            print(Data)
            fobj.close()
        else:
            print("File unable to open")
    else:
        print("File does not exists in cureent directory")

if __name__ == "__main__":
    main()