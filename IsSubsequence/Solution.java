class Solution {

    public static void main(String[] args) {
        System.out.println(isSubsequence("abc", "ahbgdc") == true);
        System.out.println(isSubsequence("axc", "ahbgdc") == false);
    }

    public static boolean isSubsequence(String s, String t) {
        int s_ind = 0;
        int t_ind = 0;

        while (t_ind < t.length()) {
            if (s.charAt(s_ind) == t.charAt(t_ind)) {
                s_ind ++;
            }
            t_ind ++;
        }

        return s_ind >= s.length();
    }
}
