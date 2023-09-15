#include<iostream>
#include<cstring>
using namespace std;
class MyString
{
    public:
    char s1[100]; 
    char s2[100];

    MyString(const char Sentence1[],const char Sentence2[])
    {
            strcpy(s1,Sentence1);
            strcpy(s2,Sentence2);
    }
    void operator+()
    {
        cout<<"Concatenation is: "<<strcat(s1,s2);
    }
};

int main()
{
    char sentence1[100],sentence2[100];
    cout<<"Enter the first sentence: ";
    cin.getline(sentence1,sizeof(sentence1));
    cout<<"first line is: "<<sentence1<<endl;

    cout<<"Enter the second sentence: ";
    cin.getline(sentence2,sizeof(sentence2));
    cout<<"first line is:"<<sentence2<<endl;

    MyString add(sentence1,sentence2);

    +add;




}