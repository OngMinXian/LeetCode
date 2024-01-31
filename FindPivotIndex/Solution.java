class Solution {

    public static void main(String[] args) {
        int arr1[] = {1,7,3,6,5,6};
        System.out.println(pivotIndex(arr1) == 3);

        int arr2[] = {1,2,3};
        System.out.println(pivotIndex(arr2) == -1);

        int arr3[] = {2,1,-1};
        System.out.println(pivotIndex(arr3) == 0);
    }

    public static int pivotIndex(int[] nums) {
        int pivot = 0;

        int left_sum = 0;
        int right_sum = 0;
        for (int i = 1; i < nums.length; i++) {
            right_sum += nums[i];
        }

        while (pivot < nums.length) {
            if (left_sum == right_sum) {
                return pivot;
            } else  {
                left_sum += nums[pivot];
                pivot ++;
                if (pivot == nums.length) { break; }
                right_sum -= nums[pivot];
            }
        }

        return -1;

    }
}
