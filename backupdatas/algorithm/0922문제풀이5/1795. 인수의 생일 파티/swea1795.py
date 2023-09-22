# swea 1795. 인수의 생일 파티
import heapq
import sys
sys.stdin = open("swea1795input.txt")

def dijkstra(start, dist):
    pq = []
    heapq.heappush(pq, (0, start))
    dist[start] = 0

    while pq:
        w, now = heapq.heappop(pq)

        if dist[now] < w:
            continue
        dist[now] = w

        for next in graph[now]:
            next_node = next[0]
            weight = next[1]

            if dist[next_node] > w + weight:
                dist[next_node] = w+weight
                heapq.heappush(pq, (w+weight, next_node))


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))
    INF = int(1e9)
    # 인수 집으로 가는 가장 짧은 거리
    to_x = [INF] * (N+1)
    # 인수 집에서 본인 집으로 가는 가장 짧은 거리
    from_x = [INF] * (N+1)
    dijkstra(X, to_x)

    for i in range(1, N+1):
        if i != X:
            dist = [INF] * (N+1)
            dijkstra(i, dist)
            from_x[i] = dist[X]
    result = 0
    # print(from_x)
    # print(to_x)
    for i in range(1, N+1):
        if i != X:
            result = max(result, to_x[i] + from_x[i])
    print(f'#{tc} {result}')