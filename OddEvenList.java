import java.util.*;

public class OddEvenList {
    public static List<String> oddOrEvenList(int[] numbers) {
        List<String> results = new ArrayList<>();
        for (int num : numbers) {
            results.add(num + " → " + (num % 2 == 0 ? "Even" : "Odd"));
        }
        return results;
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4, 5, 10};
        System.out.println(oddOrEvenList(nums));
    }
}
