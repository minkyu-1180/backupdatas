# 백준 11779. 최소 비용 구하기2
import heapq
import sys
sys.stdin = open("bj11779input.txt")

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if now == end or distance[now] < dist:
            continue
        for next in graph[now]:
            next_node = next[0]
            next_dist = next[1]

            if distance[next_node] > next_dist + dist:
                distance[next_node] = next_dist + dist
                # 그 전에 왔던 길 저장
                prev[next_node] = now
                heapq.heappush(pq, (next_dist+dist, next_node))

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

start, end = map(int, input().split())
INF = int(1e9)
distance = [INF] * (N+1)
prev = [0] * (N+1)
dijkstra(start)

result1 = distance[end]

result3 = [end]
while end != start:
    result3.append(prev[end])
    end = prev[end]
result2 = len(result3)
print(result1)
print(result2)
print(*result3[::-1])
# print(visited)
