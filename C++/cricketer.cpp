#include<iostream>
using namespace std;

// WAP: Assume a class cricketer is declared. Declare a derived class batsman from cricketer.
// Data member of batsman: Total runs, Average runs, and Best performance.
// Member functions: input data, calculate average runs, Display data. (Single Inheritance)

class cricketer
{
protected:
    int total_runs;
    int avg_runs;
    int best_performance;

public:
    // Constructor to initialize members
    cricketer(int total = 0, int avg = 0, int best = 0)
    {
        total_runs = total;
        avg_runs = avg;
        best_performance = best;
    }
};

class batsman : public cricketer
{
public:
    void input_data(int a, int b, int c)
    {
        total_runs = a;
        avg_runs = b;
        best_performance = c;
    }

    void display()
    {
        cout << "Total runs: " << total_runs << endl;
        cout << "Average runs: " << avg_runs << endl;
        cout << "Best performance: " << best_performance << endl;
    }
};

int main()
{
    int total_runs, avg_runs, best_performance;
    cout << "Enter total runs, average runs, and best performance: " << endl;
    cin >> total_runs >> avg_runs >> best_performance;

    batsman dhoni;
    dhoni.input_data(total_runs, avg_runs, best_performance);
    dhoni.display();

    return 0;
}
