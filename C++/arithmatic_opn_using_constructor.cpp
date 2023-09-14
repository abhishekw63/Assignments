#include<iostream>
using namespace std;

class arithmatic_operations
{
        protected:
        float num1,num2;

        public:
        arithmatic_operations(float x,float y)
        {
            num1=x;
            num2=y;
        }
        float addition()
        {
            return num1+num2;
        }
        float substraction()
        {
            return num1-num2;
        }

};

class multiplication :public arithmatic_operations  //derived class
{   public:
    multiplication(float a,float b) :arithmatic_operations(a,b){}
    
    float peform_multiplication()
    {
        return num1*num2;
    }

};
class division : public arithmatic_operations
{
    public:
    division (float x,float y) : arithmatic_operations(x,y)
    {}
    float perform_division()
    {
        if(num2!=0)
        {
            return num1/num2;
        }
        else
        { 
            cout<<"invalid input"<<endl;
        }
    }
};
int main()
{   float num1,num2;
    cout<<"enter two numbers";
    cin>>num1>>num2;

    arithmatic_operations obj1(num1,num2);

    cout<<"Addition is "<<obj1.addition()<<endl;
    cout<<"substraction is "<<obj1.substraction()<<endl;

    multiplication obj2(num1,num2);
    cout<<"multiplication is "<<obj2.peform_multiplication()<<endl;

    division obj3(num1,num2);
    cout<<"Division is "<<obj3.perform_division()<<endl;

    return 0;
}