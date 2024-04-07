"""
Please follow below rules while designing automation script as
• Accept input through command line or through file.
• Display any message in log file instead of console.
• For separate task define separate function.
• For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.
    1. Design automation script which accept directory name and display checksum of all files.
        
        Usage DirectoryChecksum.py "Demo"

        Demo is name of directory
    
"""

################################################
# Python import packages
################################################
import os
from sys import argv
import hashlib


################################################
# Function Name : hashfile 
# Description : generate checksum by reading file
# Input : fname, blocksize = 1024
# Output : Genetae checksum hasher.hexdigest()
# Author : Narendra Mahadev Kachare
# Date : 5/11/2023
################################################

def hashfile(fname,blocksize = 1024):
    afile = open(fname,"rb")
    buf = afile.read(blocksize)
    hasher = hashlib.md5()
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    return hasher.hexdigest()

################################################
# Function Name : DisplayChecksum 
# Description : function travel directory and display checksum
# Input : DirName
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 5/11/2023
################################################
def DisplayCheckSum(DirName):
    flag = os.path.isabs(DirName)
    if flag == False:
        DirName = os.path.abspath(DirName)
    exist = os.path.isdir(DirName)
    if exist == True:
        for foldername, subfoldername, filename in os.walk(DirName):
            print("Current foldername is : ",foldername)
            for fname in filename:
                fname = os.path.join(foldername,fname)
                file_hash = hashfile(fname)
                print(file_hash)
    else:
        print("folder or Directory does not exists")
            
        
################################################
# Function Name : main 
# Description : from where  execution starts
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 5/11/2023
################################################
def main():
    print("---------------Automation Script---------------")

    print("Application name is : ",argv[0])

    if len(argv) == 2:
        if(argv[1] == "-u" or argv[1] == "-U"):
            print("Usages : Name_of_script First_argument")
            print("Example : DirectoryChecksum.py 'Marvellous' ")
            exit()
        if(argv[1] == "-h" or argv[1] == "-H"):
            print("These script  accept directory name and display checksum of all files")
            exit()
        else:
            Arr = DisplayCheckSum(argv[1])

    else:
        print("Invalid number of argumnets or Invalid Input")


################################################
# Starter
################################################

if __name__ == "__main__":
    main()