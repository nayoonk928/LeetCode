class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(left, right, path, result):
            if len(path) == 2 * n: 
                result.append(path)
                return
            
            if left < n: 
                backtrack(left + 1, right, path + '(', result)
            if right < left:  
                backtrack(left, right + 1, path + ')', result)
        
        result = []
        backtrack(0, 0, '', result)  
        
        return result