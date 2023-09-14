#include<iostream>
using namespace std;

class Calculator    //class defination
{
    public:
    float a,b;      //attributes

    Calculator(float num1,float num2)   //constructor with parameters to intialize a and b
    {
        a=num1;
        b=num2;
    }
    float add();    //member functions
    float sub();
    float div();
    float mul();
    


};
float Calculator::add()
{
    return a+b;
}
float Calculator::sub()
{
    return a-b;
}
float Calculator::div()
{
        if(b==0)
        {
            cout<<"invalid result";
        }
        else
        {
            return a/b;
        }
}

   float Calculator::mul()
{
    return a*b;
}

int main()
{   float num1,num2;
    int choice;
   
    cout<<"PROGRAMME TO DISPLAY SIMPLE CALCULATOR USING CLASS"<<endl;
    cout<<"1.ADDITION 2.SUBSTRACTION 3.DIVISION 4.MULTIPLICATION"<<endl;
    cin>>choice;
   
    cout<<"ENTER TWO VALUES";
    cin>>num1>>num2;

    Calculator Calc(num1,num2); //create an instance of class
    
     switch(choice)
    {
        case 1:
        cout<<"summation is"<<Calc.add();   //calling the member function
        break;

        case 2:
        cout<<"substraction is"<<Calc.sub();
        break;

        case 3:
        cout<<"division is"<<Calc.div();
        break;

        case 4:
        cout<<"multiplication is "<<Calc.mul();
        break;

        default:
        cout<<"invalid output";
        break;

    }
    return 0;
}