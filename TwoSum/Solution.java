import java.util.HashMap;

class Solution {

    public static void main(String[] args) {
        int arr1[] = {2,7,11,15};
        System.out.println(twoSum(arr1, 9)[0]);
        System.out.println(twoSum(arr1, 9)[1]);

        int arr2[] = {3,2,4};
        System.out.println(twoSum(arr2, 6)[0]);
        System.out.println(twoSum(arr2, 6)[1]);

        int arr3[] = {3,3};
        System.out.println(twoSum(arr3, 6)[0]);
        System.out.println(twoSum(arr3, 6)[1]);
    }

    public static int[] twoSum(int[] nums, int target) {
        int res[] = new int[2];
        HashMap<Integer, Integer> counts = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (counts.containsKey(target - nums[i])) {
                res[0] = i;
                res[1] = counts.get(target - nums[i]);
                break;
            }
            counts.put(nums[i], i);
        }
        return res;
    }
}
