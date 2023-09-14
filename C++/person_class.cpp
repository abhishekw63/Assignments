    #include<iostream>
    #include<string.h>

    using namespace std;
    class Person
    {
        protected:
        string name;
        int age;
        
        public:
        Person()
        {
            name="NULL";
            age=0;
        }
        void set(string input_name,int input_age)
        {
            name=input_name;
            age=input_age;
        }
        void get()
        {
            cout<<"Name is "<<name<<" and age is "<<age<<endl;
        }
    
    };
    class Student : public Person
    {
        private:
        float percentage;
    
        public:
        Student()
        {
            percentage=0;
        }

        void set(float input_percentage)
        {
            percentage=input_percentage;
        }
        void get()
        {
            cout<<"Student's percentage is "<<percentage<<endl;
        }

    };
    class Teacher: public Person
    {
        private:
        int salary;

        public:
        Teacher()
        {
            salary=0;
        }
        
        void set(int input_salary)
        {
            salary=input_salary;
        }
        void get()
        {  
            cout<<"Salary is "<<salary;
        }
    };

    int main()
    {   string input_name;
        int input_age;
        int input_percentage;
        int input_salary;

        Student raj;
        cout<<"enter student name, age and percentage";
        cin>>input_name>>input_age>>input_percentage;
        raj.Person::set(input_name,input_age);
        raj.set(input_percentage);
        raj.Person::get();
        raj.get();

        Teacher maheshsir;
        cout<<"Enter the teacher's name and age and salary";
        cin>>input_name>>input_age>>input_salary;
        maheshsir.Person::set(input_name,input_age);
        maheshsir.set(input_salary);
        maheshsir.Person::get();
        maheshsir.get();
    } 