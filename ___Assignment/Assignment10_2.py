"""
Please follow below rules while designing automation script as
• Accept input through command line or through file. Display any message in log file instead of console.
• For separate task define separate function.
• For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.

    1. Design automation script which accept directory name and two file extension from user.
    Rename all files with first file extension with the second file extension
    
    Usage : DirectoryRename.py "Demo" ".txt" ".doc"
    
    Demo is name of directory and .txt is the extension that we want to search.

    
"""
################################################
# Required Python Packages
################################################
from sys import *
import os
import time 



################################################
# Function Name : CreateDirectory 
# Description : DirectoryRename
# Input : DirName,extention1,extension2
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 29/10/2023
################################################
def DirectoryRename(DirName,extention1,extension2):
    print("We are searching the directory with name : ",DirName)
    name = ""
    extention = ""

    flag = os.path.isabs(DirName)

    if flag == False:
        DirName = os.path.abspath(DirName)
    
    exist = os.path.isdir(DirName)
    if exist:
        for foldername, subfoldername, filename in os.walk(DirName):
            for fname in filename:
                fname = os.path.join(foldername,fname)
                
                if fname.endswith(extention1):
                    
                    name, extention = os.path.splitext(fname)
                    os.replace(src=(name+extention),dst=(name+extension2))
        print("Files are successfully renamed")

    else:
        print("Directory are not exists")

################################################
# Function Name : main 
# Description : main function from where execution starts
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 29/10/2023
################################################
def main():
    print("-------------------Automation Script------------------")

    if(argv[1] == "-u" or argv[1] == "-U"):
        print("Usage : Name_of_Script <DirName> <extention1> <extention2>")
        print("Example : DirectoryRename.py Demo  '.txt'  '.doc' ")
        exit()

    if(argv[1] == "-h" or argv[1] == "-H"):
        print("These script is used to replace 1st extention input with second second extension")
        exit()
    
    if len(argv) != 4:
        print("Invalid number of arguments")
        exit()
    else:
        StartT = time.time()
        DirectoryRename(argv[1],argv[2],argv[3])
        EndT = time.time()
        print("Time required to excute the script is : ",EndT-StartT)


#################################################
# Application Starter
#################################################
if __name__ == "__main__":
    main()