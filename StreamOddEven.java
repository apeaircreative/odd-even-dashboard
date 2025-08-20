import java.util.Scanner;

public class StreamOddEven {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter numbers (type 'quit' to stop):");

        while (true) {
            String input = scanner.nextLine();
            
            if (input.equalsIgnoreCase("quit")) {
                System.out.println("Stream ended.");
                break;
            }

            try {
                int num = Integer.parseInt(input);
                System.out.println(num + " → " + (num % 2 == 0 ? "Even" : "Odd"));
            } catch (NumberFormatException e) {
                System.out.println("Please enter a valid number or 'quit'.");
            }
        }
        scanner.close();
    }
}
