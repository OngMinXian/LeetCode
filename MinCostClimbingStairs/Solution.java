import java.lang.Math;

class Solution {

    public static void main(String[] args) {
        int arr1[] = {10,15,20};
        System.out.println(minCostClimbingStairs(arr1) == 15);

        int arr2[] = {1,100,1,1,1,100,1,1,100,1};
        System.out.println(minCostClimbingStairs(arr2) == 6);
    }

    public static int minCostClimbingStairs(int[] cost) {
        int dp[] = new int[cost.length + 1];
        for (int i = 0; i <= cost.length; i++) {
            dp[i] = 0;
        }
        
        for (int i = 2; i <= cost.length; i++) {
            dp[i] = Math.min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1]);
        }
        return dp[cost.length];
    }
}
