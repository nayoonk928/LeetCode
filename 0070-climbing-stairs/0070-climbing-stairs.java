class Solution {
    public int climbStairs(int n) {
        // 제약 : 한 번에 1칸 또는 2칸을 올라갈 수 있음
        // 구현 :
        // - dp[n] = dp[n - 1] + dp[n - 2];
        // - 초기값 할당
        //  - dp[1] = 1;
        //  - dp[2] = 2;
    
        int[] dp = new int[n + 1];
        
        if (n >= 1) {
            dp[1] = 1;
        } 
        
        if (n >= 2) {
            dp[2] = 2;
        }

        if (n == 1 || n == 2) {
            return dp[n];
        }
        
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        return dp[n];
    }
}