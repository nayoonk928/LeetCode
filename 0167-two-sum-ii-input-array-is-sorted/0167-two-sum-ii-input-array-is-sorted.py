class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binary_search(start, end):
            while start < end:
                add = numbers[start] + numbers[end]
    
                if add == target:
                    return [start + 1, end + 1]
                elif add < target:
                    start += 1
                else:
                    end -= 1
    
        return binary_search(0, len(numbers) - 1)