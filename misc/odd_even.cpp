#include <iostream>
using namespace std;

string oddOrEven(int num) {
    return (num % 2 == 0) ? "Even" : "Odd";
}

int main() {
    cout << oddOrEven(10) << endl; // Output: Even
    cout << oddOrEven(7) << endl;  // Output: Odd
    return 0;
}
