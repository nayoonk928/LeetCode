class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        answer = []
        heap = []  # min heap -> (1의 개수, index)
        
        for idx, mat_row in enumerate(mat):
            count_ones = mat_row.count(1)
            heapq.heappush(heap, (count_ones, idx))
        
        for _ in range(k):
            count_ones, idx = heapq.heappop(heap)
            answer.append(idx)
            
        return answer