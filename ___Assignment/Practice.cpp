#include<iostream>
using namespace std;

class Array
{   
    public:
    int iSize;
    int *ptr;

    Array(int X)
    {
        iSize = X;
        ptr = new int[iSize];
    }
    ~Array()
    {
        delete ptr;
    }
    void Accept()
    {
        int iCnt = 0;
        cout<<"Enter elements : \n";
        for(iCnt = 0; iCnt < iSize; iCnt++)
        {
            cin>>ptr[iCnt];
        }
    }    
    void Display()
    {
        int iCnt = 0;
        for (iCnt = 0; iCnt < iSize; iCnt++)
        {
            cout<<ptr[iCnt]<<"\t";
        }
        cout<<"\n";
    }
    int Addition()
    {
        int Ans = 0,iCnt = 0;
        for (iCnt = 0; iCnt < iSize; iCnt++)
        {
            Ans = Ans + ptr[iCnt];
        }
        return Ans;
    }
    int Maximum()
    {
        int No = 0;
        for (int iCnt = 0; iCnt < iSize; iCnt++)
        {
            if (ptr[iCnt] > No)
            {
                No = ptr[iCnt];
            }
            
        }
        return No;
        
    }
};


int main()
{
    int iValue = 0;
    int iRet = 0;

    cout<<"Enter the number of elements\n";
    cin>>iValue;
    Array aobj(iValue);

    aobj.Accept();
    aobj.Display();
    iRet = aobj.Addition();
    cout<<"Addition of the given elements are : "<<iRet<<"\n";

    iRet = aobj.Maximum();
    cout<<"Maximum number of the given elements is : "<<iRet<<"\n";


    
    return 0;
}