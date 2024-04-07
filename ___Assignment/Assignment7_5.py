"""

5. Design python application which contains two threads named as thread1 and thread2. Thread1 display 1 to 50 on screen and
thread2 display 50 to 1 in reverse order on screen. After execution of thread1 gets completed then schedule thread2.

"""
import threading

def Increment(No):
    print(threading.current_thread())
    for i in range(1,No,1):
        print(i,end=" ")
    print()

def Decrement(No):
    print(threading.current_thread())
    for i in range(No-1,0,-1):
        print(i,end=" ")
    print()

def main():
    print("Demonstration of Increment-Decrement order of threads")

    Value = 1+int(input("Enter Number : \n"))
    # Create thread
    T1 = threading.Thread(args = (Value,), target = Increment)
    T2 = threading.Thread(args = (Value,), target = Decrement)

    # Start thread
    T1.start()
    T1.join()
    T2.start()
    T2.join()

    # wait for thread





if __name__ == "__main__":
    main()