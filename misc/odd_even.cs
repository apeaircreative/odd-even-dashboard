using System;

class Program {
    static string OddOrEven(int num) {
        return (num % 2 == 0) ? "Even" : "Odd";
    }

    static void Main() {
        Console.WriteLine(OddOrEven(10)); // Output: Even
        Console.WriteLine(OddOrEven(7));  // Output: Odd
    }
}
