class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        black_count = s.count('1')
        white_count = n - black_count
        steps = 0
        black_seen = 0
    
        for ball in s:
            if ball == '1':
                black_seen += 1
            else:
                steps += black_seen
    
        return steps