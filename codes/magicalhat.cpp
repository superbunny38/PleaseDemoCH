#include <iostream>
#include <string>
using namespace std;

void sortingHat() {
    int bravery = 0, loyalty = 0, intelligence = 0, ambition = 0;
    string answer;

    cout << "Welcome to the Hogwarts Sorting Hat Ceremony!" << endl;
    cout << "Answer the following questions to find out which house you belong to." << endl;

    // Question 1
    cout << "\nQuestion 1: What would you do if you found a lost item?\n";
    cout << "a) Return it to its owner.\n";
    cout << "b) Keep it for yourself.\n";
    cout << "c) Study it to learn more about it.\n";
    cout << "d) Use it to your advantage.\n";
    cout << "Enter your choice (a/b/c/d): ";
    cin >> answer;
    if (answer == "a") loyalty++;
    else if (answer == "b") ambition++;
    else if (answer == "c") intelligence++;
    else if (answer == "d") bravery++;

    // Question 2
    cout << "\nQuestion 2: What is your favorite activity?\n";
    cout << "a) Exploring new places.\n";
    cout << "b) Helping others.\n";
    cout << "c) Reading books.\n";
    cout << "d) Competing in challenges.\n";
    cout << "Enter your choice (a/b/c/d): ";
    cin >> answer;
    if (answer == "a") bravery++;
    else if (answer == "b") loyalty++;
    else if (answer == "c") intelligence++;
    else if (answer == "d") ambition++;

    // Question 3
    cout << "\nQuestion 3: What quality do you value the most?\n";
    cout << "a) Courage.\n";
    cout << "b) Kindness.\n";
    cout << "c) Wisdom.\n";
    cout << "d) Determination.\n";
    cout << "Enter your choice (a/b/c/d): ";
    cin >> answer;
    if (answer == "a") bravery++;
    else if (answer == "b") loyalty++;
    else if (answer == "c") intelligence++;
    else if (answer == "d") ambition++;

    // Determine the house
    cout << "\nThe Sorting Hat has made its decision...\n";
    if (bravery >= loyalty && bravery >= intelligence && bravery >= ambition) {
        cout << "You belong to Gryffindor!" << endl;
    } else if (loyalty >= bravery && loyalty >= intelligence && loyalty >= ambition) {
        cout << "You belong to Hufflepuff!" << endl;
    } else if (intelligence >= bravery && intelligence >= loyalty && intelligence >= ambition) {
        cout << "You belong to Ravenclaw!" << endl;
    } else {
        cout << "You belong to Slytherin!" << endl;
    }
}

int main() {
    sortingHat();
    return 0;
}