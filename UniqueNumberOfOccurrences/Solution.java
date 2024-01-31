import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

class Solution {

    public static void main(String[] args) {
        int arr1[] = {1,2,2,1,1,3};
        System.out.println(uniqueOccurrences(arr1) == true);

        int arr2[] = {1,2};
        System.out.println(uniqueOccurrences(arr2) == false);

        int arr3[] = {-3,0,1,-3,1,1,1,-3,10,0};
        System.out.println(uniqueOccurrences(arr3) == true);
    }

    public static boolean uniqueOccurrences(int[] arr) {
        HashMap<Integer, Integer>  hm = new HashMap<>();

        for (int i = 0; i < arr.length; i++) {
            hm.put(arr[i], hm.getOrDefault(arr[i], 0) + 1);
        }

        HashSet<Integer> counts = new HashSet<>();
        for (Map.Entry<Integer, Integer> entry : hm.entrySet()) {
            counts.add(entry.getValue());
        }

        return counts.size() == hm.size();
    }
}
