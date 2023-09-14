#include<iostream>
using namespace std;

double mathOperation(double num1,double num2)
{
        return num1+num2;
}
double mathOperation(double num1,double num2,char minus)
{
    return num1-num2;
    
}
double mathOperation(double num1,double num2,int multiplication)
{
    return num1*num2;
    
}
double mathOperation(double num1,double num2,bool division)
{
    if(num2!=0)
    {
    return num1/num2;
    }
    else
    {
        cout<<"Division is not possible";
    }
    
}

int main()
{   double num1,num2;
    char choice;

    cout<<"Enter two numbers";
    cin>>num1>>num2;
    
    cout<<"Enter your choice"<<endl;
    cout<<"+ for addition"<<endl<<"- For substraction"<<endl<<"* For multiplication"<<endl<<"/ for division";
    cin>>choice;

    switch(choice)
    {
        case '+':
        cout<<mathOperation( num1, num2);
        break;

        case '-':
        cout<<mathOperation( num1, num2,'-');
        break;
        
        case '*':
        cout<<mathOperation( num1, num2,1);
        break;

        case '/':
        cout<<mathOperation( num1, num2,true);
        break;

        default:
        cout<<"Invalid operation choice"<<endl;
        break;
    }
}