class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n  # 결과를 저장할 리스트 초기화
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # 현재 날짜의 기온이 스택에 저장된 날짜의 기온보다 높을 때
                last_date = stack.pop()
                result[last_date] = i - last_date  # 현재 날짜와의 차이를 저장
    
            stack.append(i)  # 현재 날짜를 스택에 추가
    
        return result
        