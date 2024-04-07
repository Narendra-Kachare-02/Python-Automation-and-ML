"""
Please follow below rules while designing automation script as
• Accept input through command line or through file. Display any message in log file instead of console.
• For separate task define separate function.
• For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.

    1. Design automation script which accept two directory names and one file extension.
    copy all files from first directory into second directory. second directory should be created at run time
    
    Usage : DirectoryCopyExt.py "Demo" "Temp" ".exe"
    
    Demo is name of directory which is existing and contains files in it. We have to create new 
    Directory as Temp and copy all files with extension .exe from Demo to Temp
    
"""
################################################
# Required Python Packages
################################################

import os
import time
from sys import *
import shutil

################################################
# Function Name : CreateDirectory 
# Description : Create Directory
# Input : DirName1 i.e argv[2]
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 29/10/2023
################################################

def CreateDirectory(DirName1):
    try:
        os.makedirs(DirName1,mode=0o777)
        print("Directory successfully created")
    except FileExistsError as fobj:
        print("Error : ",fobj)

################################################
# Function Name : DirectoryCopyExt 
# Description : Copy files from one directory to second directory with specified extension
# Input : DirName,T_folder,extention
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 29/10/2023
################################################

def DirectoryCopyExt(DirName,T_folder,extention):
    flag = os.path.isabs(DirName)

    if flag == False:
        DirName = os.path.abspath
    
    exist = os.path.isdir(DirName)
    CreateDirectory(T_folder)
    
    if exist:
        for foldername, subfoldername, filename in os.walk(DirName):
            for fname in filename:
                
                fname = os.path.join(foldername,fname)
                if fname.endswith(extention):
                    shutil.copy(fname,T_folder)
        print("Specified Extension Data Successfully copied from one into another")
                

################################################
# Function Name : main 
# Description : main function from where execution starts
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 29/10/2023
################################################

def main():
    print("--------------Automation Script--------------")

    if len(argv) == 2:
        if(argv[1] == "-u" or argv[1] == "-U"):
            print("Usage : Name_of_script First_argument Second_argumnet Third_argument")
            print("Example : DirectoryCopyExt.py Demo  Temp  .exe")
            exit()
        elif(argv[1] == "-h" or argv[1] == "-H"):
            print("Copy all files with specified extensions from one directory to another directory")
            exit()   
    if(len(argv) != 4):
        print("Invalid number of arguments")
        exit()
    else:
        StartT = time.time()
        DirectoryCopyExt(argv[1],argv[2],argv[3])
        EndT = time.time()
        print("Time required to execute the code is : ",EndT-StartT)
    



#################################################
# Application Starter
#################################################

if __name__ == "__main__":
    main()


