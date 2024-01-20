class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((v, w))

        dist = [int(1e9)] * (n + 1)
        dist[k] = 0

        pq = [(0, k)]

        while pq:
            time, node = heapq.heappop(pq)

            if time > dist[node]:
                continue

            for adj, w in graph[node]:
                cost = time + w
                if cost < dist[adj]:
                    dist[adj] = cost
                    heapq.heappush(pq, (cost, adj))

        max_dist = max(dist[1:])
        return max_dist if max_dist < int(1e9) else -1