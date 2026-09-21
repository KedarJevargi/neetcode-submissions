class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq

        adj_list = {}

        for i in range(1, n + 1):
            adj_list[i] = []

        for u, v, t in times:
            adj_list[u].append((v, t))

        def dijkstra(adj_list, source, n):
            dist = [float('inf')] * (n + 1)
            dist[source] = 0

            heap = [(0, source)]

            while heap:
                curr_dist, u = heapq.heappop(heap)

                if curr_dist > dist[u]:
                    continue

                for v, weight in adj_list[u]:
                    new_dist = curr_dist + weight

                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        heapq.heappush(heap, (new_dist, v))

            return dist

        dist = dijkstra(adj_list, k, n)

        max_time = 0

        for i in range(1, n + 1):
            if dist[i] == float('inf'):
                return -1

            max_time = max(max_time, dist[i])

        return max_time