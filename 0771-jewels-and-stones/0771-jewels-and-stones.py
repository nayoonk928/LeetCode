class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:        
        count = 0
        for stone in list(stones):
            if stone in set(jewels):
                count += 1
        
        return count
        