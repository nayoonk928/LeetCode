class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_num = heapq.nlargest(1, nums)[-1]
        second_max_num = heapq.nlargest(2, nums)[-1]
        return (max_num - 1)*(second_max_num - 1)
    