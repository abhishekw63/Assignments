#include<iostream>
using namespace std;

class Matrix
{
    public:
    int size_input;
    int data[100];

    Matrix(int sz)
    {
        size_input=sz;
    }

    Matrix operator+(const Matrix& m2)
    {   Matrix m3(size_input);
        for(int i=0;i<size_input;i++)
        {
            m3.data[i]=data[i]+ m2.data[i];
        }
        return m3;
    }
};

int main()
{   int size1,size2;
    cout<<"Enter the size of matrix 1 and 2:";
    cin>>size1>>size2;

    if(size1!=size2)
    {
        cout<<"Addition coudnt perform because of size mismatch";
        return -1;
    }
    else
    {
        Matrix M1(size1);
        Matrix M2(size2);

        cout<<"Enter the element of matrix 1: ";
        for(int i=0;i<size1;i++)
        {
        cin>>M1.data[i];
        }
        cout<<endl;
        cout<<"Enter the element of matrix 2: ";
        for(int i=0;i<size1;i++)
        {
        cin>>M2.data[i];
        }
       
        Matrix M3=M1 + M2;

        cout<<"Addition is:";
        for(int i=0;i<size1;i++)
        {
            cout<<M3.data[i]<<" ";
        }
        return 0;
    }
}