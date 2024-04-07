"""

2. Design python application which creates two threads as evenfactor and oddfactor. 
Both the thread accept one parameter as integer. Evenfactor thread will display addition of 
even factors of given number and oddfactor will display addition of odd factors of given number. 
After execution of both the thread gets completed main thread should display message as "exit from main".

"""

import threading
import queue

def EvenFactor(No,q):
    Ans = 0
    for i in range(1,int(No/2)):
        if No % i == 0:
            if i % 2 == 0:
                print(i)
                Ans = Ans + i
    q.put(Ans)

def OddFactor(No,q):
    Ans = 0
    for i in range(1,int(No/2)):
        if No % i == 0:
            if i % 2 != 0:
                print(i)
                Ans = Ans + i
    q.put(Ans)


def main():
    print("Demostration of EvenFactor OddFactor thread")

    Q = queue.Queue()

    Value = int(input("Enter number : "))

    # Create thread
    T1 = threading.Thread(args=(Value,Q,),target=EvenFactor)
    T2 = threading.Thread(args=(Value,Q,),target=OddFactor)

    # Start thread
    T1.start()
    T2.start()

    # wait thread
    T1.join()
    T2.join()

    # Fetch the queue values from loop
    i = 1
    while Q.empty() is False:
        print("Task",i,"Addition is :",end=" " )
        print(Q.get())
        print("\n")
        i+=1


if __name__ == "__main__":
    main()

