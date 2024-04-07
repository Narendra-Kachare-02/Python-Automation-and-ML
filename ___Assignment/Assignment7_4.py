"""

4. Design python application which creates three threads as small, capital, digits. All the threads accepts
string as parameter. Small thread display number of small characters, capital thread display number of capital 
characters and digits thread display number of digits. Display id and name of each thread.

"""
import threading
import queue

def Digit(cArr,q):
    print(threading.current_thread())
    iCnt = 0
    for i in cArr:
        if ord(i) >= ord('0') and ord(i) <= ord('9'):
            iCnt+=1
    q.put(iCnt)

def Capital(cArr,q):
    print(threading.current_thread())
    iCnt = 0
    for i in cArr:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            iCnt+=1
    q.put(iCnt)
    

def Small(cArr,q):
    print(threading.current_thread())
    iCnt = 0
    for i in cArr:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            iCnt+=1
    q.put(iCnt)
    



def main():
    print("Demonstration of Small-Captial-Digit Thread")

    Str = str(input("Enter string : "))
    Q = queue.Queue()

    # Create thread
    T1 = threading.Thread(args=(Str,Q),target=Digit)
    T2 = threading.Thread(args=(Str,Q),target=Capital)
    T3 = threading.Thread(args=(Str,Q),target=Small)
    
    # Start thread
    T1.start()
    T2.start()
    T3.start()

    # wait for remaining thread
    T1.join()
    T2.join()
    T3.join()

    Arr = ['Digit','Capital','Small']
    i = 0
    while Q.empty() is False:
        print(Arr[i]," Count will be : ",Q.get())
        i+=1



   



if __name__ == "__main__":
    main()