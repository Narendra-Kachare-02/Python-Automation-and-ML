"""
Please follow below rules while designing automation script as

• Accept input through command line or through file.
• Display any message in log file instead of console.
• For separate task define separate function.
• For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.

    2. Design automation script which accept Directory name from user and create log file in that directory which 
    contains information of running processes as its name, PID, username

    Usage : ProcInfoLog.py Demo

"""
################################################
# Python import modules
################################################
from sys import *
import os
import psutil
from time import ctime, time

################################################
# Function Name : Directory 
# Description : function create logfile inside directory
# Input : DirName
# Output : logpath
# Author : Narendra Mahadev Kachare
# Date : 20/11/2023
################################################
def Directory(DirName):
    exist = os.path.isabs(DirName)
    if exist == False:
        DirName = os.path.abspath(DirName)
    
    flag = os.path.isdir(DirName)
    if flag == False:
        print("Directory is not found")
        os.mkdir(DirName)
        print("We create directory in current Path")
    else:
        print("Directory found")

    # return logpath
    return os.path.join(DirName,"logfile"+str(time())+".txt")

################################################
# Function Name : ProcInfo 
# Description : function accept process and display information of that process
# Input : PName
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 20/11/2023
################################################
def ProcInfoLog(logpath):
    
    separator = "-"*84+"\n"

    # Create log file
    afile = open(logpath,"w")
    print("logfile Successfully created")


    afile.write(separator+"Process Automation : "+str(ctime()).replace(" ","_").replace(":",".")+"\n"+separator)


    # fetch process, minimize data, append in list
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(['name','pid','username'])
            afile.write(str(pinfo)+"\n")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    # close logfile
    afile.close()
    print("Process information successfully copied inside logfile")


################################################
# Function Name : main 
# Description : function where execution starts
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 20/11/2023
################################################
def main():
    print("Process Automation Script")
    if(len(argv) != 2):
        print("Invalid number of arguments")
        exit()
    
    if(argv[1] == "u" or argv[1] == "-U"):
        print("Usage : Name_of_Script DirName")
        print("Example : ProcInfo.py Demo")
        exit()

    if(argv[1] == "h" or argv[1] == "-H"):
        print("These script  accept foldername and write process information inside log file inside folder")
        exit()
    try:
        logpath = Directory(argv[1])
        
    except ValueError:
        print("Error : Invalid datatype of input")
        exit()
    
    except Exception as e:
        print("Error : ",e)
        exit()

    ProcInfoLog(logpath)
    

################################################
# Starter kit
################################################
if __name__ == "__main__":
    main()