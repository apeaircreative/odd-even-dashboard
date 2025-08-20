import java.util.Random;

public class AutoStreamOddEven {
    public static void main(String[] args) throws InterruptedException {
        Random rand = new Random();
        System.out.println("Starting automated Odd/Even stream... (Press Ctrl+C to stop)");

        while (true) {
            int num = rand.nextInt(100) + 1; // 1 to 100
            System.out.println(num + " → " + (num % 2 == 0 ? "Even" : "Odd"));
            Thread.sleep(1000); // wait 1 second
        }
    }
}
