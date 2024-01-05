class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counters = collections.Counter(nums)
        most_frequency = counters.most_common(k)
        
        return [item[0] for item in most_frequency]