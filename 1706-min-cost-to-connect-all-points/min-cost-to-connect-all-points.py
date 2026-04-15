import heapq

class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        visited = [False] * n
        min_dist = [float('inf')] * n
        min_dist[0] = 0

        heap = [(0, 0)]  # (cost, point_index)
        result = 0

        while heap:
            cost, u = heapq.heappop(heap)

            if visited[u]:
                continue

            visited[u] = True
            result += cost

            for v in range(n):
                if not visited[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])

                    if dist < min_dist[v]:
                        min_dist[v] = dist
                        heapq.heappush(heap, (dist, v))

        return result