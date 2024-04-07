"""
Please follow below rules while designing automation script as
• Accept input through command line or through file.
• Display any message in log file instead of console.
• For separate task define separate function.
• For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.
    1. Design automation script which accept directory name and delete all duplicate files from that 
       Directory write names of duplicate files from that directory named as log.txt
       Log.txt file should be created into current directory Display execution time required for the script
        
        Usage DirectoryDuplicateRemoval.py "Demo"

        Demo is name of directory

"""

################################################
# Python import packages
################################################
import os
from sys import argv
import time
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
# Output : function return dictionary having checksums and their filenames
# Author : Narendra Mahadev Kachare
# Date : 5/11/2023
################################################
def DisplayCheckSum(DirName):
    dups = {}
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
                if file_hash in dups:
                    dups[file_hash].append(fname)
                else:
                    dups[file_hash] = [fname]
        return dups

    else:
        print("Folder or Directory does not exists")

################################################
# Function Name : CreateLogfile 
# Description : function cretes logile having duplicate file names
# Input : Dict1 (Dictionary having hascode and values)
# Output :  
# Author : Narendra Mahadev Kachare
# Date : 11/11/2023
################################################
def CreateLogfile(Dict1):
    Dict1 = dict(Dict1)
    sep = "-"*84

    # Create log file
    afile = open("Logfile.txt","a")
    
    afile.write(sep+"\n")
    afile.write(time.ctime()+"\n")
    afile.write(sep+"\n")

    for Eachlist in Dict1.values():
        if len(Eachlist) >= 2:
            for path in Eachlist[1:]:
                afile.write(path)
                os.remove(path)
                afile.write("\n")
    afile.close()
    
    print("log file Successfully created")
################################################
# Function Name : DeleteDuplicate 
# Description : function delete duplicate files
# Input : DirName
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 11/11/2023
################################################
def DeleteDuplicate(Dict1):
    Dict1 = dict(Dict1)
    flag = False

    # Delete Duplicate file
    for Eachlist in Dict1.values():
        if len(Eachlist) >= 2:
            for path in Eachlist[1:]:
                flag = True
                os.remove(path)
    if flag == True:
        print("Duplicate files Successfully Deleted")
    else:
        print("No Dplicate files are found")
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
            StartT = time.time()
            Dict = DisplayCheckSum(argv[1])
            CreateLogfile(Dict)
            DeleteDuplicate(Dict)
            EndT = time.time()
            print("Time required to execute the code is : ",EndT-StartT)

    else:
        print("Invalid number of argumnets")


################################################
# Starter
################################################

if __name__ == "__main__":
    main()