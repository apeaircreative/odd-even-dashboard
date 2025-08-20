import java.util.*;

public class SplitOddEven {
    public static Map<String, List<Integer>> splitOddEven(int[] numbers) {
        List<Integer> evens = new ArrayList<>();
        List<Integer> odds = new ArrayList<>();

        for (int num : numbers) {
            if (num % 2 == 0) {
                evens.add(num);
            } else {
                odds.add(num);
            }
        }

        Map<String, List<Integer>> result = new HashMap<>();
        result.put("Evens", evens);
        result.put("Odds", odds);
        return result;
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4, 5, 10};
        Map<String, List<Integer>> result = splitOddEven(nums);
        System.out.println("Evens: " + result.get("Evens"));
        System.out.println("Odds: " + result.get("Odds"));
    }
}
