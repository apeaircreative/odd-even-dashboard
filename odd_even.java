public class OddEvenCheck {
    public static String oddOrEven(int num) {
        return (num % 2 == 0) ? "Even" : "Odd";
    }

    public static void main(String[] args) {
        System.out.println(oddOrEven(10)); // Output: Even
        System.out.println(oddOrEven(7));  // Output: Odd
    }
}
