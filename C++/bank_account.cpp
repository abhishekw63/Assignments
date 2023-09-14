#include<iostream>
#include<string.h>
using namespace std;

class SBI      //defination of class
{
   private:
   long acc_num;     //attributes(member variable)
   long acc_balance;
   long acc_deposit;
   long acc_withdraw;

   public:
   string acc_name;
   string acc_type;

   SBI(long a,long b)      // Constructor to initialize account number and balance
   {
      acc_num=a;
      acc_balance=b;
   }

   void display();      //member function defination. Display account information
   void deposit(long x);  
   void withdraw(long x);
   void balance();
};
void SBI::display()     //member function
{
     cout<<"Account Name:"<<acc_name<<endl;
      cout<<"Account type:"<<acc_type<<endl;
      cout<<"Account Number:"<<acc_num<<endl;
      cout<<"Account Balance:"<<acc_balance;
}
void SBI::deposit(long x)
{
   if(x>0)
      {

      acc_deposit=x;
      cout<<endl<<"amount deposited "<<acc_deposit<<endl;
      }
      else
      {
         cout<<"Invalid amount transaction"<<endl;
      }
}
void SBI::withdraw(long x)
{
   if(x>0 && x<acc_balance)
      {
      acc_withdraw=x;
      cout<<"amount withdrawed "<<acc_withdraw<<endl;
      }
      else
      {
         cout<<"Insufficient amount"<<endl;
      }
}
void SBI:: balance()
   {
      acc_balance=acc_balance+acc_deposit-acc_withdraw;
   }
int main()
{
   SBI abhi(98791542,100000);    //object creation
   abhi.acc_name="Abhishek Wagh";
   abhi.acc_type="Saving";

   cout<<"INTITAL INFORMATION"<<endl;
   abhi.display();

   long depo;
   cout<<endl<<"enter amount to be deposited";

   cin>>depo;
   abhi.deposit(depo);

   long with;
   cout<<"enter amount to be withdraw";
   cin>>with;
   abhi.withdraw(with);

   abhi.balance();

   cout<<endl<<"Updated information."<<endl;
   abhi.display();
}