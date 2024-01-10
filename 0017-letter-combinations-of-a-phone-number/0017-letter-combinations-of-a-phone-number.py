class Solution:  
    def letterCombinations(self, digits: str) -> List[str]:
        chars = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        if not digits:
            return []
    
        result = []
    
        def dfs(digit, current_path):
            if not digit:
                result.append("".join(current_path))
                return
    
            current_digit = digit[0]
            for char in chars[current_digit]:
                dfs(digit[1:], current_path + [char])
    
        dfs(list(digits), [])
        return result
        