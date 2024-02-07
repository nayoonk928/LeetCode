class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        reversed_x = 0
        negative = x < 0
        x = abs(x)

        while x != 0:
            digit = x % 10  # x의 일의 자리 숫자
            # 결과값이 32비트 정수의 최대값을 초과하거나, 최대값에 도달하고 현재 숫자가 7보다 크면 overflow가 발생하므로 0을 반환
            if reversed_x > INT_MAX // 10 or (reversed_x == INT_MAX // 10 and digit > 7):
                return 0
            # 결과값이 32비트 정수의 최소값을 초과하거나, 최소값에 도달하고 현재 숫자가 -8보다 작으면 overflow가 발생하므로 0을 반환
            if reversed_x < INT_MIN // 10 or (reversed_x == INT_MIN // 10 and digit < -8):
                return 0
            reversed_x = reversed_x * 10 + digit  # 현재 결과값에 현재 숫자를 추가하여 결과값을 갱신
            x //= 10  # x를 10으로 나누어 다음 자릿수로 이동


        return -reversed_x if negative else reversed_x
