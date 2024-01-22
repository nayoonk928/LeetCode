class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def divide_and_conquer(nums, left, right):
            if left == right:
                return nums[left]

            mid = (left + right) // 2

            # 왼쪽, 오른쪽, 가로지르는 중간 부분 배열에서 얻을 수 있는 최대 연속 부분 배열의 합
            left_max = divide_and_conquer(nums, left, mid)
            right_max = divide_and_conquer(nums, mid + 1, right)
            cross_max = max_cross_sum(nums, left, mid, right)

            return max(left_max, right_max, cross_max)

        def max_cross_sum(nums, left, mid, right):
            left_sum = float('-inf')
            current_sum = 0

            for i in range(mid, left - 1, -1):
                current_sum += nums[i]
                left_sum = max(left_sum, current_sum)

            right_sum = float('-inf')
            current_sum = 0

            for i in range(mid + 1, right + 1):
                current_sum += nums[i]
                right_sum = max(right_sum, current_sum)

            return left_sum + right_sum

        if not nums:
            return 0

        return divide_and_conquer(nums, 0, len(nums) - 1)
