"""
Please follow below rules while designing automation script as

• Accept input through command line or through file.
• Display any message in log file instead of console.
• For separate task define separate function.
• For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.

    2. Design automation script which accept process name and display information of that process if it is running

    Usage : ProcInfo.py Notepad

"""
################################################
# Python import modules
################################################
from sys import *
import psutil

################################################
# Function Name : ProcInfo 
# Description : function accept process and display information of that process
# Input : PName
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 20/11/2023
################################################
def ProcInfo(PName):
    # Create empty process
    listprocess = []

    # fetch process, minimize data, append in list
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(['name','pid','username'])
            if(pinfo['name'] == PName+".exe" or pinfo['name'] == PName):
                listprocess.append(pinfo)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    # return process
    return listprocess


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
        print("Usage : Name_of_Script Process_name")
        print("Example : ProcInfo.py Notepad")
        exit()

    if(argv[1] == "h" or argv[1] == "-H"):
        print("These script is accept process name and display information of that process\nIf process is running ")
        exit()

    listprocess = ProcInfo(argv[1])
    if len(listprocess) == 0:
        print(argv[1]+" process : Not Active")
        exit()
    else:
        print(argv[1]+" process : Active\nBelow is the process information")

        for elements in listprocess:
            print(elements)

################################################
# Starter kit
################################################
if __name__ == "__main__":
    main()