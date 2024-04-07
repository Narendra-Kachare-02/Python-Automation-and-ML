"""
    write a program which accepts two file names from user and compare contents of both the
    files if both files contents are sane the Display success otherwise display failure.
    Accept file name through command line arguments


    Input : Demo.txt     Hello.txt
    Create new file as Demo.txt and copy contents of ABC,txt in Demo.txt

"""
from sys import argv
import os

def main():
    print("Demonstration of FileIO")

    if (argv[1] == '-u' or argv[1] == '-U'):
        print("Copy below code\nNote : fill Sourcee and Dest file names on your own\n","  %s S_file D_file  "%argv[0])
        return


    Source_File = argv[1] # ABC.txt
    Dest_File = argv[2]   # Demo.txt

    
    # Read file
    if os.path.exists(Source_File and Dest_File):
        fobj1 = open(Source_File,"r")
        if fobj1:
            print("Source file successfully opened")
        fobj2 = open(Dest_File,"r")
        if fobj2:
            print("Dest file successfully opened")


        if fobj1 and fobj2:
            Data1 = fobj1.read()
            Data2 = fobj2.read()
            fobj1.close()
            fobj2.close()
            print("Source & Dest file Successfully Read")
        else:
            print("File Unable to Open")
    else:
        print("file not Exists error")
    
    if os.path.exists(Source_File and Dest_File):
        if (Data1 == Data2):
            print("Both files content are same")
        else:
            print("Both files are not same")


if __name__ == "__main__":
    main()