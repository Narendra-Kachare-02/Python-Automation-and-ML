"""
Please follow below rules while designing automation script as
• Accept input through command line or through file. Display any message in log file instead of console.
• For separate task define separate function.
• For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.

    1. Design automation script which accept directory name and file extension from user. Display all files with that extension.
    
    Usage : Directory FileSearch.py "Demo" ".txt"
    
    Demo is name of directory and .txt is the extension that we want to search.

    
"""
################################################
# Required Python Packages
################################################
from sys import *
import os
import time 


################################################
# Function Name : DirectoryFileSearch 
# Description : DirectoryRename
# Input : DirName,extention
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 29/10/2023
################################################
def DirectoryFileSearch(DirName,extention):
    print("We are searching the directory with name : ",DirName)
    flag = os.path.isabs(DirName)

    if flag == False:
        DirName = os.path.abspath(DirName)
    
    exist = os.path.isdir(DirName)
    if exist:
        for foldername, subfoldername, filename in os.walk(DirName):
            print("Current directory name is : ",foldername)
            for fname in filename:
                fname = os.path.join(foldername,fname)
                if fname.endswith(extention):
                    print(fname)
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
        print("Usage : Name_of_Script <DirName> <extention>")
        print("Example : DirectoryFileSearch.py Demo .txt")
        exit()

    if(argv[1] == "-h" or argv[1] == "-H"):
        print("These script accept two argument as DirName and extention and display all that extension files in that directory ")
        exit()
    
    if len(argv) != 3:
        print("Invalid number of arguments")
        exit()
    else:
        StartT = time.time()
        DirectoryFileSearch(argv[1],argv[2])
        EndT = time.time()
        print("Time required to excute the script is : ",EndT-StartT)

#################################################
# Application Starter
#################################################
if __name__ == "__main__":
    main()