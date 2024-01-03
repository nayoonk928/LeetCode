class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 결과를 저장할 리스트 초기화
        result = []
        # 입력 배열을 정렬
        nums.sort()
    
        # 첫 번째 숫자를 기준으로 반복
        for i in range(len(nums) - 2):
            # 중복된 첫 번째 숫자는 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue
    
            # 두 번째와 세 번째 숫자를 가리킬 포인터 초기화
            left, right = i + 1, len(nums) - 1
    
            # 투 포인터를 사용하여 합을 찾기
            while left < right:
                total = nums[i] + nums[left] + nums[right]
    
                # 합이 0보다 작으면 왼쪽 포인터를 증가
                if total < 0:
                    left += 1
                # 합이 0보다 크면 오른쪽 포인터를 감소
                elif total > 0:
                    right -= 1
                # 합이 0이면 결과에 추가하고 중복된 값을 건너뛰기
                else:
                    result.append([nums[i], nums[left], nums[right]])
    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
    
                    left += 1
                    right -= 1

        return result

# 시간 복잡도: O(n^2)
