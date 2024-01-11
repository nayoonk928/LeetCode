class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def get_subset(start, current_subset):
            result.append(current_subset[:])
    
            for i in range(start, len(nums)):
                current_subset.append(nums[i])
                get_subset(i + 1, current_subset)
                current_subset.pop()
    
        get_subset(0, [])
        return result