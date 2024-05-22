class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return cnt.most_common()[-1][0]