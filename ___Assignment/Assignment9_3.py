
from sys import argv
import os

class FileSystem:

    def __init__(self):
        self.Source_File = argv[1] # ABC.txt
        self.Dest_File = argv[2]   # Demo.txt
    
    def Create(self):
        if os.path.exists(self.Dest_File):
            print("File already exists")    # Demo.txt
        else:
            fobj = open(self.Dest_File,"x")
            fobj.close()
            print("Destination file Successfully Created")

    def Read(self):
        if os.path.exists(self.Source_File):
            fobj = open(self.Source_File,"r")
            if fobj:
                Data = fobj.read()
                fobj.close()
                print("Source file Successfully Read")
                return Data
            else:
                print("File Unable to Open")
        else:
            print("Source file not Exists")

    def Write(self):
        if os.path.exists(self.Dest_File):
            fobj = open(self.Dest_File,"w")
            if fobj:
                iRet = self.Read()
                fobj.write(iRet)
                fobj.close()
                print("Source file Successfully read and Written in Destination file")
            else:
                print("Dest file Unable to Open")
        else:
            print("Destination file not Exists")
    
    def ReadData(self):
        fobj = open(self.Dest_File,"r")
        print(fobj.read())
    
    

def main():
    obj1 = FileSystem()
    obj1.Create()
    obj1.Write()
    obj1.ReadData()

if __name__ == "__main__":
    main()