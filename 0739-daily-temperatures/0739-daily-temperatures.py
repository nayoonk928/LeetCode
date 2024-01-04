class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n 
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                last_date = stack.pop()
                result[last_date] = i - last_date 
    
            stack.append(i) 
    
        return result
        