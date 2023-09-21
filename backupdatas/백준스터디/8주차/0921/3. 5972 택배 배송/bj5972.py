# 백준 5972. 택배 배송
import heapq
import sys
sys.stdin = open("bj5972input.txt")

def dijkstra(start):
    pq = []

    heapq.heappush(pq, (0, start))
    dist[start] = 0

    while pq:
        w, now = heapq.heappop(pq)
        if dist[now] < w:
            continue
        dist[now] = w

        for next_node, weight in graph[now]:
            if dist[next_node] <= w + weight:
                continue
            dist[next_node] = w + weight
            heapq.heappush(pq, (w+weight, next_node))



N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

dist = [int(1e9)] * (N+1)
dijkstra(1)
print(dist[N])

