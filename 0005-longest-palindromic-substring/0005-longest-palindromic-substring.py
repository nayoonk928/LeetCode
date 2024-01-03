class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 주어진 문자열이 비어있으면 빈 문자열 반환
        if len(s) == 0:
            return ""

        # 팰린드롬의 시작과 끝을 나타내는 변수 초기화
        start, end = 0, 0

        # 주어진 문자열의 각 위치를 중심으로 확장하는 방법을 사용
        for i in range(len(s)):
            # 현재 위치를 중심으로 하는 홀수 길이 팰린드롬의 길이
            len1 = self.expand(s, i, i)
            
            # 현재 위치와 오른쪽의 위치를 중심으로 하는 짝수 길이 팰린드롬의 길이
            len2 = self.expand(s, i, i + 1)
            
            # 두 길이 중에서 더 긴 팰린드롬의 길이 선택
            max_len = max(len1, len2)
    
            # 현재 팰린드롬이 더 긴 경우, 시작과 끝을 갱신
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
    
        # 시작부터 끝까지의 부분 문자열이 가장 긴 팰린드롬
        return s[start:end + 1]
    
    def expand(self, s: str, left: int, right: int) -> int:
        # 현재 중심에서 팰린드롬이 확장될 수 있는 한 확장
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
    
        # 현재 팰린드롬의 길이 반환
        return right - left - 1
