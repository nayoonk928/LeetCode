class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((v, w))
    
        dist = [int(1e9)] * len(graph)
    
        pq = []
        heapq.heappush(pq, (0, k))
        dist[k] = 0
    
        while pq:
            time, node = heapq.heappop(pq)
    
            if dist[node] < time:
                continue
    
            for adj, w in graph[node]:
                cost = time + w
                if cost < dist[adj]:
                    dist[adj] = cost
                    heapq.heappush(pq, (cost, adj))
    
        if all(dist[i] != int(1e9) for i in range(1, len(dist))):
            return max(dist[1:])
        else:
            return -1