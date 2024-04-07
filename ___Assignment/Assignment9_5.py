"""


    Accept file name and one string from user and return the frequecy of that string from file.

    Input : Demo.txt    Marvellous
    Search "Marvellous" in Demo.txt
"""
from sys import argv
import os

def main():
    print("Demonstration of FileIO")

    iCnt = 0
    file_name = argv[1] # ABC.txt
    Word = argv[2]    # Marvellous
    

    if (argv[1] == "-u" or argv[1] == "-U"):
        print("  %s f_name <String>  "%argv[0])
        return
   

    # Read file
    if os.path.exists(file_name):
        fobj = open(file_name,"r") 
        if fobj:
            Data = fobj.read()
            fobj.close()
        else:
            print("File unable to open")
    else:
        print("File not exists")

    # Read word from file
    for line in Data.split():
        if line == Word:
            iCnt+=1
    print("Frequecy of '"+argv[2]+"' is %d" %iCnt)
       



if __name__ == "__main__":
    main()