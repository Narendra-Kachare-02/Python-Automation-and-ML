"""
Please follow below rules while designing automation script as
• Accept input through command line or through file. Display any message in log file instead of console.
• For separate task define separate function.
• For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.

    1. Design automation script which accept two directory names.
    copy all files from first directory into second directory. second directory should be created at run time
    
    Usage : DirectoryCopy.py "Demo" ".txt" ".doc"
    
    Demo is name of directory and .txt is the extension that we want to search.

    
"""
################################################
# Required Python Packages
################################################
import os
from sys import *
import time
import shutil


################################################
# Function Name : CreateDirectory 
# Description : DirectoryCopy
# Input : DirName,DirName1
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 29/10/2023
################################################

def DirectoryCopy(DirName,DirName1):

    flag = os.path.isabs(DirName)
    if flag == False:
        DirName = os.path.abspath(DirName)
    
    exist = os.path.isdir(DirName)
    if exist:
        for foldername, subfoldername, filename in os.walk(DirName):
            for fname in filename:
                fname = os.path.join(foldername,fname)
                shutil.copy(src=fname,dst=DirName1)
        print("File successfully copied")
    else:
        print("File does not exists")

################################################
# Function Name : main 
# Description : main function from where execution starts
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 29/10/2023
################################################
def main():
    print("---------------Automation Script---------------")

    if (len(argv) == 2):
        if (argv[1] == "-u" or argv[1] == "-U"):
            print("Usage : Name_of_Script First_argument Second_argument")
            print("Example : Demo.py Marvellous Temp")
            exit()
        elif(argv[1] == "-h" or argv[1] == "-H"):
            print("These script is copy directory files from one to another")
            exit()
        
    if(len(argv) != 3):
        print("Invalid number of arguments")
        exit()
    else:
        StartT = time.time()
        DirectoryCopy(argv[1],argv[2])
        EndT = time.time()
        print("Timw required to execute the code is : ",EndT-StartT)

#################################################
# Application Starter
#################################################

if __name__ == "__main__":
    main()