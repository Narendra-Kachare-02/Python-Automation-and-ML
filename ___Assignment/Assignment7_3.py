"""

3. Design python application which creates two threads as evenlist and odd list. Both the threads accept list
of integers as parameter. Evenlist thread add all even elements from input list and display the addition. Oddlist 
thread add all odd elements from input list and display the addition.

"""

import threading
import queue

def EvenList(ptr,q):
    Ans = 0
    for No in ptr:
        if(No % 2 == 0):
            Ans = Ans + No
    q.put(Ans)
        

def OddList(ptr,q):
    Ans = 0
    for No in ptr:
        if(No % 2 != 0):
            Ans = Ans + No
    q.put(Ans)        


def main():
    print("Demostration of EvenFactor OddFactor thread")

    print("Enter the number of elements : ")
    Length = int(input())

    Q = queue.Queue()
    Arr = list()

    print("Enter the elements : ")
    for Value in range(0,Length):
        Value = int(input())
        Arr.append(Value)
    

    # Create thread
    T1 = threading.Thread(args=(Arr,Q,),target=EvenList)
    T2 = threading.Thread(args=(Arr,Q,),target=OddList)

    # Start thread
    T1.start()
    T2.start()

    # wait thread
    T1.join()
    T2.join()

    # Fetch the queue values from loop
    i = 1
    while Q.empty() is False:
        print("Task%d Addition is : "%i,Q.get())
        i+=1 
    

if __name__ == "__main__":
    main()

