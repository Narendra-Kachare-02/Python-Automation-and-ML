"""
Design python application which creates two threads named as even and odd. Even thread will display
first 10 even numbers and odd thread will display first 10 odd numbers.

"""
import threading

def Even(No):
    
    print("Even number : \n",threading.current_thread())
    for i in range(0,No,2):
        print(i,end="\t")
    print("\n")

def Odd(No):
    print("Odd number : \n",threading.current_thread())
    for i in range(1,No,2):
        print(i,end="\t")
    print("\n")
    



def main():
    print("Demonstration of Even odd thread")
    Value = int(input("Upto Display करायचे आहेत पहिले Odd Even Number :"))
    Value = Value*2
    
    # Create thread
    T1 = threading.Thread(args= (Value,),target = Even)
    T2 = threading.Thread(args= (Value,),target = Odd)

    # Initialise thread 
    T1.start()
    T2.start()

    # Wait until thread process done
    T1.join()
    T2.join()
    


if __name__ == "__main__":
    main()