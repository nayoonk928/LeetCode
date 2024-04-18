class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # 오른쪽부터 시작하여 nums[i] < nums[i+1]을 만족하는 첫 번째 인덱스 i를 찾기
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # 이러한 인덱스 i가 존재하면, i 오른쪽에서 nums[i]보다 큰 첫 번째 숫자를 찾기
        # 그리고 이를 nums[i]와 교환
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # i+1부터 끝까지의 서브 배열을 뒤집기
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
