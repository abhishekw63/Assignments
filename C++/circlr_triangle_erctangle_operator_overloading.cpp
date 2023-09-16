/*Write a program to calculate the area of circle, rectangle and triangle using 
Function Overloading 
 Rectangle: Area * breadth -- length *breadth
 Triangle: ½ *Area* breadth  -- base*height
 Circle: Pi * Area *Area*/    // --  radius*radius

#include<iostream>
using namespace std;
#define PI 3.14 

class Calculation
{
    private:
    float Length;
    float Breadth;
    float Base;
    float Height;
    float Radius;

    public:
    Calculation()
    {
        Length=0;
        Breadth=0;
        Base=0;
        Height=0;
        Radius=0;
        
    }
    float FunctionOverloading(double l,double b)
    {
        Length=l;
        Breadth=b;
        return Length*Breadth;
    }
    float FunctionOverloading(float H,float BS,bool isTraingle=0)
    {
        if(isTraingle==0)
        {
        Height=H;
        Base=BS;
        return 0.5*Height*Base;
         }
         else
         {
                cout<<"Compiler fails to diffrentiate triangle";
                return 0;
         }
    }
    float FunctionOverloading(float r,char circle)
    {
        if(circle=='Y')
        {
        Radius=r;
        return PI*Radius*Radius;
        }
        
    }



};
int main()
{
    float height,base,radius;
    double length,breadth;
    bool isTriangle;
    char isCircle='Y';
    Calculation Operation;
   
    cout<<"enter the length and breadth";
    cin>>length>>breadth;
    cout<<"The area of rectangle is: "<<Operation.FunctionOverloading(length,breadth)<<endl;

    cout<<"Is it triangle? "<<"enter 0 for YES or 1 for false";
    cin>>isTriangle;
    if(isTriangle==0)
    {
        cout<<"enter the value of base and height";
        cin>>base>>height;
        cout<<"The area of traingle  is: "<<Operation.FunctionOverloading(base,height,isTriangle)<<endl;
    }
   
    cout<<"Enter the value of radius";
    cin>>radius;
     cout<<"The area of circle  is: "<<Operation.FunctionOverloading(radius,isCircle)<<endl;






}