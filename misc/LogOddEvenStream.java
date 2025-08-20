package misc;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class LogOddEvenStream {
    public static void main(String[] args) throws InterruptedException {
        Random rand = new Random();
        System.out.println("Streaming numbers... Logging to evens.txt and odds.txt (Press Ctrl+C to stop)");

        while (true) {
            int num = rand.nextInt(100) + 1;
            try {
                if (num % 2 == 0) {
                    FileWriter fw = new FileWriter("evens.txt", true);
                    fw.write(num + "\n");
                    fw.close();
                    System.out.println(num + " → Even");
                } else {
                    FileWriter fw = new FileWriter("odds.txt", true);
                    fw.write(num + "\n");
                    fw.close();
                    System.out.println(num + " → Odd");
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
            Thread.sleep(1000);
        }
    }
}
