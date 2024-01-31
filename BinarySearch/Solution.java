class Solution {

    public static void main(String[] args) {
        int arr1[] = {-1,0,3,5,9,12};
        System.out.println(search(arr1, 9) == 4);

        int arr2[] = {-1,0,3,5,9,12};
        System.out.println(search(arr2, 2) == -1);
    }

    public static int search(int[] nums, int target) {
        int low = 0;
        int high = nums.length;
        int mid = 0;

        while (low <= high) {
            mid = (low + high) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                high = mid - 1;
            } else if (nums[mid] < target) {
                low = mid + 1;
            }
        }
        return -1;
    }
}
