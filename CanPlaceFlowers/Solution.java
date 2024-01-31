class Solution {

    public static void main(String[] args) {
        int array[] = {1, 0, 0, 0, 1};
        System.out.println(canPlaceFlowers(array, 1) == true);
        System.out.println(canPlaceFlowers(array, 2) == false);
    }

    public static boolean canPlaceFlowers(int[] flowerbed, int n) {
        int place = 0;
        for (int i = 0; i < flowerbed.length; i++) {
            if (i == 0) {
                if (flowerbed[i] == 0) {
                    place ++;
                    flowerbed[i] = 1;
                }
            } else {
                if (flowerbed[i - 1] == 0 && flowerbed[i] == 0) {
                    place ++;
                    flowerbed[i] = 1;
                } else if (flowerbed[i - 1] == 1 && flowerbed[i] == 1) {
                    place --;
                }
            }
        }
        return place == n;
    }
}
