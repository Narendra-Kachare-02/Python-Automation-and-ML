"""
    write a program which accepts file name from user and check whether that file exists in current directory or not.

    Input : Demo.txt
    Check whether Demo.txt exists or not.

"""
import os

def main():

    # Accept file
    File_name = input("Enter file name : \n")
    
    # Check file exists or not.
    if os.path.exists(File_name):
        print("File Already exists")
    else:
        print("File not exists in cureent directory")

if __name__ == "__main__":
    main()