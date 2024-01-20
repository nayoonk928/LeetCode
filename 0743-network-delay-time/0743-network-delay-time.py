class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((v, w)) 
        
        dist = [int(1e9)] * (n + 1)
    
        pq = []
        heapq.heappush(pq, (0, k))
        dist[0] = 0
        dist[k] = 0
    
        cnt = 1
        while pq:
            time, node = heapq.heappop(pq)
    
            if dist[node] < time:
                continue
    
            for adj, w in graph[node]:
                cost = time + w
                if cost < dist[adj]:
                    if dist[adj] == int(1e9):
                        cnt += 1
                    dist[adj] = cost
                    heapq.heappush(pq, (cost, adj))
    
        if cnt == n:
            return max(dist)
    
        return -1