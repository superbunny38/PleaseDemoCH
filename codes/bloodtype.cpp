#include <iostream>
#include <set>
#include <string>
using namespace std;

// Function to determine possible blood types of a child
set<string> getPossibleBloodTypes(const string& mom, const string& dad) {
    set<string> possibleBloodTypes;

    // Blood type inheritance rules
    if ((mom == "A" && dad == "A") || (mom == "A" && dad == "O") || (mom == "O" && dad == "A")) {
        possibleBloodTypes.insert("A");
        possibleBloodTypes.insert("O");
    }
    if ((mom == "B" && dad == "B") || (mom == "B" && dad == "O") || (mom == "O" && dad == "B")) {
        possibleBloodTypes.insert("B");
        possibleBloodTypes.insert("O");
    }
    if ((mom == "A" && dad == "B") || (mom == "B" && dad == "A")) {
        possibleBloodTypes.insert("A");
        possibleBloodTypes.insert("B");
        possibleBloodTypes.insert("AB");
        possibleBloodTypes.insert("O");
    }
    if ((mom == "AB" && dad == "A") || (mom == "A" && dad == "AB")) {
        possibleBloodTypes.insert("A");
        possibleBloodTypes.insert("B");
        possibleBloodTypes.insert("AB");
    }
    if ((mom == "AB" && dad == "B") || (mom == "B" && dad == "AB")) {
        possibleBloodTypes.insert("A");
        possibleBloodTypes.insert("B");
        possibleBloodTypes.insert("AB");
    }
    if ((mom == "AB" && dad == "AB")) {
        possibleBloodTypes.insert("A");
        possibleBloodTypes.insert("B");
        possibleBloodTypes.insert("AB");
    }
    if ((mom == "AB" && dad == "O") || (mom == "O" && dad == "AB")) {
        possibleBloodTypes.insert("A");
        possibleBloodTypes.insert("B");
    }
    if ((mom == "O" && dad == "O")) {
        possibleBloodTypes.insert("O");
    }

    return possibleBloodTypes;
}

int main() {
    string mom, dad;

    // Input blood types of mom and dad
    cout << "Enter the blood type of the mom (A, B, AB, O): ";
    cin >> mom;
    cout << "Enter the blood type of the dad (A, B, AB, O): ";
    cin >> dad;

    // Get possible blood types of the child
    set<string> childBloodTypes = getPossibleBloodTypes(mom, dad);

    // Output the results
    cout << "Possible blood types of the child: ";
    for (const string& bloodType : childBloodTypes) {
        cout << bloodType << " ";
    }
    cout << endl;

    return 0;
}