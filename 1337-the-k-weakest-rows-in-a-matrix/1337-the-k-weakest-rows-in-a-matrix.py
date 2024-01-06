class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        answer = []
        mat_one_count = collections.defaultdict(int)  # index와 1의 개수 저장
        
        for idx, mat_row in enumerate(mat):
            mat_one_count[idx] = mat_row.count(1)
        
        sorted_mat_one_count = sorted(mat_one_count.items(), key=lambda x:x[1])
        
        for key, value in sorted_mat_one_count:
            answer.append(key)
            
        return answer[:k]