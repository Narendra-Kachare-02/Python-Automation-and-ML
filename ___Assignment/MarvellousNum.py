
def ChkPrime(ptr):
    Ans = 0
    for j in range(len(ptr)):
        No = ptr[j]
        i = 2
        while(i < int(No/2)+1):
            if((No % i) == 0):
                break
            i = i + 1
        if(i == int(No/2)+1):
            Ans = Ans + ptr[j]
    return Ans
 