#include <iostream>
#include <tuple>
using namespace std;

// Function to perform addition, subtraction, multiplication, and division
tuple<double, double, double, double> calculate(double a, double b) {
    double addition = a + b;
    double subtraction = a - b;
    double multiplication = a * b;
    double division = (b != 0) ? (a / b) : 0; // Handle division by zero
    return make_tuple(addition, subtraction, multiplication, division);
}

int main() {
    double a, b;

    // Input two numbers
    cout << "Enter the first number (a): ";
    cin >> a;
    cout << "Enter the second number (b): ";
    cin >> b;

    // Get the results
    auto [addition, subtraction, multiplication, division] = calculate(a, b);

    // Output the results
    cout << "Addition: " << addition << endl;
    cout << "Subtraction: " << subtraction << endl;
    cout << "Multiplication: " << multiplication << endl;
    if (b != 0) {
        cout << "Division: " << division << endl;
    } else {
        cout << "Division: Undefined (division by zero)" << endl;
    }

    return 0;
}