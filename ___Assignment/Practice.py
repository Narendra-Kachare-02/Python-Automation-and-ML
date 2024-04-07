"""
Please follow below rules while designing automation script as

• Accept input through command line or through file.
• Display any message in log file instead of console.
• For separate task define separate function.
• For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.

    2. Design automation script which accept Directory name and mail id from user and create log file in that directory which contains 
    informations of runnig processes as its name, pid, username. After creating log file send that file to the specified mail

    Usage : ProcInfoLog.py Demo Marvellousinfosystem@gmail.com

    Demo is name of Directory.
    marvellousinfosystem@gmail.com is the mail id.

"""
MB = 1024* 1024
################################################
# Python import modules
################################################
from sys import *
import os
import psutil
from time import ctime, time
from urllib import request, error

################################################
# Function Name : is_connected 
# Description : function check internet connectivity
# Input : 
# Output : boolean value (either True or False)
# Author : Narendra Mahadev Kachare
# Date : 22/11/2023
################################################
def is_connected():
    try:
        request.urlopen("https://www.youtube.com/",timeout=1)
        return True
    except error.URLError as err:
        return False

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
            pinfo['vms'] = str(proc.memory_info().vms / MB) + " MB"
            afile.write(str(pinfo)+"\n")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    # close logfile
    afile.close()
    print("Process information successfully copied inside logfile")

################################################
# Function Name : MailSender 
# Description : function create mail having (To,From,Subject,CC,Attachements) and send mail 
# Input : filename, time
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 23/11/2023
################################################

def MailSender(filename,time):
    fromaddr = "source_mail_id_@gmail.com"
    toaddr = "dest_mail-id_@gmail.com"

    

















################################################
# Function Name : main 
# Description : function where execution starts
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 20/11/2023
################################################
def main():
    
    # print("Process Automation Script")
    # if(len(argv) != 2):
    #     print("Invalid number of arguments")
    #     exit()
    
    # if(argv[1] == "u" or argv[1] == "-U"):
    #     print("Usage : Name_of_Script DirName")
    #     print("Example : ProcInfo.py Demo")
    #     exit()

    # if(argv[1] == "h" or argv[1] == "-H"):
    #     print("These script  accept Dirname and mail id from user. create running process info logfile and send logfile to the specified mail")
    #     exit()
    # try:
    #     logpath = Directory(argv[1])
        
    # except ValueError:
    #     print("Error : Invalid datatype of input")
    #     exit()
    
    # except Exception as e:
    #     print("Error : ",e)
    #     exit()

    # ProcInfoLog(logpath)

    Connection = is_connected()
    if Connection == True:
        print("Internet is on")
    else:
        print("There is no any internet connectivity")
    

################################################
# Starter kit
################################################
if __name__ == "__main__":
    main()


"""
1 byte = 8 bit
1 KB = 1024 bytes
1 MB = 1024*_1024 bytes
1 GB = 1024*_1024*_1024 bytes
1 TB = 1024*_1024*_1024*_1024 bytes
"""