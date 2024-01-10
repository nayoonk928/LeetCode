class Solution:  
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
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        result = []
        self.dfs(list(digits), [], result)
        return result
        
        
    def dfs(self, digits, current_path, result):
        # 끝까지 탐색했다면 result 반환
        if not digits:
            result.append("".join(current_path))
            return
        
        current_digit = digits[0]
        for char in self.chars[current_digit]:
            # digits의 첫 번째 원소 제외한 나머지 부분, 지금까지 저장된 문자 + 현재 문자
            self.dfs(digits[1:], current_path + [char], result)
        