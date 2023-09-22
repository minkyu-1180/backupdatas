# 백준 1916. 최소비용 구하기
import heapq
import sys
sys.stdin = open("bj1916input.txt")

def dijkstra(start):
    pq = []

    cost[start] = 0
    heapq.heappush(pq, (start, 0))

    while pq:
        now, w = heapq.heappop(pq)

        if cost[now] < w:
            continue
        cost[now] = w
        
        for next in graph[now]:
            next_node, weight = next[0], next[1]
            if cost[next_node] <= w + weight:
                continue
            cost[next_node] = w + weight
            heapq.heappush(pq, (next_node, w+weight))


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

# print(graph)
# print(pq)
start, end = map(int, input().split())

INF = int(1e9)
cost = [INF] * (N+1)
dijkstra(start)
print(cost[end])
# print(cost[end])