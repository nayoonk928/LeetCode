class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]

        # from, to, price
        for f, t, p in flights:
            graph[f].append((t, p))
    
        dist = [int(1e9)] * (n + 1)
    
        pq = []
        heapq.heappush(pq, (0, 0, src))  # (price, stops, node)
        dist[src] = 0
        visit = {}  # 방문했는지 저장
        while pq:
            price, stops, curr = heapq.heappop(pq)
    
            if curr == dst:
                return price
    
            # 방문하지 않은 노드이거나 방문한 노드라면 지나온 노드가 더 적어야 함
            if curr not in visit or visit[curr] > stops:
                visit[curr] = stops
                for adj, cost in graph[curr]:
                    if stops <= k:
                        heapq.heappush(pq, (price + cost, stops + 1, adj))
    
        return -1