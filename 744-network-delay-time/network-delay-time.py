import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = {i: [] for i in range(1, n+1)}

        # строим граф
        for u, v, w in times:
            graph[u].append((v, w))

        # минимальные расстояния
        dist = {i: float('inf') for i in range(1, n+1)}
        dist[k] = 0

        heap = [(0, k)]  # (время, узел)

        while heap:
            time, node = heapq.heappop(heap)

            if time > dist[node]:
                continue

            for nei, w in graph[node]:
                new_time = time + w

                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(heap, (new_time, nei))

        max_time = max(dist.values())

        return max_time if max_time != float('inf') else -1