#include <iostream>
using namespace std;

class Batch
{
protected:
    string student[3];

public:
    void setStudents(string s1, string s2, string s3)
    {
        student[0] = s1;
        student[1] = s2;
        student[2] = s3;
    }
};

class Students : public Batch
{
protected:
    int roll_no[3];

public:
    void setRollNumbers(int r1, int r2, int r3)
    {
        roll_no[0] = r1;
        roll_no[1] = r2;
        roll_no[2] = r3;
    }
};

class Test : public Students
{
protected:
    int english_marks[3];
    int maths_marks[3];

public:
    void setMarks(int eng1, int maths1, int eng2, int maths2, int eng3, int maths3)
    {
        english_marks[0] = eng1;
        maths_marks[0] = maths1;

        english_marks[1] = eng2;
        maths_marks[1] = maths2;

        english_marks[2] = eng3;
        maths_marks[2] = maths3;
    }
};

class Results : public Test
{
protected:
    int total_marks[3];
    int average_marks[3];

public:
    void calculateTotalAndAverage()
    {
        for (int i = 0; i < 3; i++)
        {
            total_marks[i] = english_marks[i] + maths_marks[i];
            average_marks[i] = total_marks[i] / 2;
        }
    }

    void displayResults()
    {
        calculateTotalAndAverage();

        for (int i = 0; i < 3; i++)
        {
            cout << "Batch " << char('A') << " - Student: " << student[i] << endl;
            cout << "Roll number: " << roll_no[i] << endl;
            cout << "Marks of English: " << english_marks[i] << endl;
            cout << "Marks of Maths: " << maths_marks[i] << endl;
            cout << "Total marks: " << total_marks[i] << endl;
            cout << "Average: " << average_marks[i] << endl << endl;
        }
    }
};

int main()
{
    // Input for Batch A
    string s1, s2, s3;
    int r1, r2, r3;
    int engA1, engA2, engA3, mathsA1, mathsA2, mathsA3;

    cout << "Enter the students' names of Batch A: ";
    cin >> s1 >> s2 >> s3;

    cout << "Enter the roll numbers of students of Batch A: ";
    cin >> r1 >> r2 >> r3;

    cout << "Enter the marks for Batch A:" << endl;
    cout << "Marks of English for " << s1 << ": ";
    cin >> engA1;
    cout << "Marks of Maths for " << s1 << ": ";
    cin >> mathsA1;

    cout << "Marks of English for " << s2 << ": ";
    cin >> engA2;
    cout << "Marks of Maths for " << s2 << ": ";
    cin >> mathsA2;

    cout << "Marks of English for " << s3 << ": ";
    cin >> engA3;
    cout << "Marks of Maths for " << s3 << ": ";
    cin >> mathsA3;

    Results result;
    result.setStudents(s1, s2, s3);
    result.setRollNumbers(r1, r2, r3);
    result.setMarks(engA1, mathsA1, engA2, mathsA2, engA3, mathsA3);

    result.displayResults();
    return 0;
}
