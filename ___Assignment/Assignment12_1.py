"""
Please follow below rules while designing automation script as

• Accept input through command line or through file.
• Display any message in log file instead of console.
• For separate task define separate function.
• For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.

    1. Design automation script which display information of running processes as its name, pid, username

    Usage : ProcInfo.py

"""

################################################
# Python import packages
################################################
from sys import argv
import psutil

################################################
# Function Name : ProcInfo 
# Description : function display information of running processes as its name, pid, username
# Input :  
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 19/11/2023
################################################

def ProcInfo():
    print("Process Automation")

    # Create empty list
    listprocess = []
    # fetch process, minimize data, append in list
    for proc in psutil.process_iter():
        try : 
            pinfo = proc.as_dict(['name','username','pid'])
            listprocess.append(pinfo)
        except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
            pass

    # return list
    return listprocess



################################################
# Function Name : main 
# Description : function where execution starts
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 19/11/2023
################################################
def main():
    print("-------Automation Script---------")
    
    print("Application name : ",argv[0])
    listprocess = ProcInfo()

    for elements in listprocess:
        print(elements)


################################################
# Starter kit
################################################
if __name__ == "__main__":
    main()