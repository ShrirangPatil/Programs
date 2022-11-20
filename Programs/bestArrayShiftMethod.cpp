#include <iostream>
#include <stdint.h>
#include <string>
using namespace std;

template <class T>
class ShiftPtr 
{
private:
    T* ptr;
    uint64_t shift, size;
public:
    // Constructor
    explicit ShiftPtr(T* p = NULL, uint64_t k = 0, uint64_t n = 0) 
    { 
        ptr = p;
        shift = k%n;
        size = n;
    }
 
    ~ShiftPtr() {  }
 
    T& operator*() { return *ptr; }
 
    T* operator->() { return ptr; }
    
    T* operator+(uint64_t i)
    {
        if (i < size) 
            return ptr+((shift+i)%size);
        else
            throw "Index out of bound";
    }
    
    T& operator[](uint64_t i)
    {
        if (i < size) 
            return *(ptr+((shift+i)%size));
        else
            throw "Index out of bound";
    }
};

 
int main()
{
    cout<< "Int array" << endl;
    int arr[] = {343, 235, 22, 2433, 4};
    uint64_t n = 5, k = 999999999999;
    ShiftPtr<int> ptr(arr, k, n);
    try 
    {
        for (int i=0;i<n;i++)
        {
            cout << ptr[i] << endl;
        }
    }
    catch(const char* exception)
    {
        clog << exception<<endl;
    }

    cout << "double array" << endl;
    double doubleArr[] = {323.34, 253.903, 23.43, 21.34, 1.22322};
    uint64_t nD = 5, kD = 88888888888;
    ShiftPtr<double> ptrD(doubleArr, kD, nD);
    try 
    {
        for (int i=0;i<nD+1;i++)
        {
            cout << ptrD[i] << endl;
        }
    }
    catch(const char* exception)
    {
        clog << exception<<endl;
    }

    cout << "char array" <<endl;
    char charArr[] = {'s', 'a', '3', '0', '$'};
    uint64_t nC = 5, kC = 77777777777;
    ShiftPtr<char> ptrC(charArr, kC, nC);
    try 
    {
        for (int i=0;i<nC;i++)
        {
            cout << ptrC[i] << endl;
        }
    }
    catch(const char* exception)
    {
        clog << exception<<endl;
    }
}