public class Solution {
    public int maxSubArray(int[] nums) {
        return maxSubArray(nums, 0, nums.length - 1);
    }
    
    private int maxSubArray(int[] nums, int left, int right) {
        // 기저 사례: 배열의 길이가 1인 경우
        if (left == right) {
            return nums[left];
        }
        
        // 중간 지점 계산
        int mid = left + (right - left) / 2;
        
        // 왼쪽 부분 배열에서 최대 부분 배열 합 찾기
        int leftMax = maxSubArray(nums, left, mid);
        // 오른쪽 부분 배열에서 최대 부분 배열 합 찾기
        int rightMax = maxSubArray(nums, mid + 1, right);
        // 중간을 포함하는 부분 배열에서 최대 부분 배열 합 찾기
        int crossMax = crossMaxSubArray(nums, left, mid, right);
        
        // 세 경우 중 최대값 반환
        return Math.max(Math.max(leftMax, rightMax), crossMax);
    }
    
    // 중간을 포함하는 부분 배열에서 최대 부분 배열 합을 찾는 함수
    private int crossMaxSubArray(int[] nums, int left, int mid, int right) {
        // 왼쪽 반부터 시작하여 최대 부분 배열 합 계산
        int leftMax = Integer.MIN_VALUE;
        int sum = 0;
        for (int i = mid; i >= left; i--) {
            sum += nums[i];
            leftMax = Math.max(leftMax, sum);
        }
        
        // 오른쪽 반부터 시작하여 최대 부분 배열 합 계산
        int rightMax = Integer.MIN_VALUE;
        sum = 0;
        for (int i = mid + 1; i <= right; i++) {
            sum += nums[i];
            rightMax = Math.max(rightMax, sum);
        }
        
        // 중간을 포함하는 부분 배열에서의 최대 부분 배열 합 반환
        return leftMax + rightMax;
    }
}
