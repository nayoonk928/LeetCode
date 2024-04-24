public class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0]; // 현재까지의 최대 부분 배열 합
        int currentSum = nums[0]; // 현재까지의 부분 배열 합

        // 배열을 순회하면서 최대 부분 배열 합을 찾음
        for (int i = 1; i < nums.length; i++) {
            // 현재 원소를 현재까지의 부분 배열 합에 더함
            currentSum = Math.max(nums[i], currentSum + nums[i]);
            // 현재까지의 최대 부분 배열 합 갱신
            maxSum = Math.max(maxSum, currentSum);
        }

        return maxSum;
    }
}
