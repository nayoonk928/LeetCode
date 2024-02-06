class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        insert_idx = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[insert_idx] = nums[i]
                insert_idx += 1
        
        return insert_idx