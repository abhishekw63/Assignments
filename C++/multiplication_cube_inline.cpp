#include<iostream>
using namespace std;

/*WAP TO FIND MULTIPLICATION AND CUBIC VALUES USING INLINE FUNCTION*/

inline float multi(float num1,float num2)
{
    return num1*num2;
}
inline float Cube(int num)
{
    return num*num*num;
}
int main()
{
    float num1,num2,input_cube;
    cout<<"enter two values";
    cin>>num1>>num2;
    cout<<"multiplication is "<<multi(num1,num2)<<endl;
    cout<<"enter the value to get cube of:";
    cin>>input_cube;
    cout<<"cube is "<<Cube(input_cube);



}
