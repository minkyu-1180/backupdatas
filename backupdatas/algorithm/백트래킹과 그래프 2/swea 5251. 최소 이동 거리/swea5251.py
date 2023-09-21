# swea 5251. 최소 이동 거리
import sys
sys.stdin = open("swea5251input.txt")
import heapq

def dijkstra(start):
    pq = []
    pq.append((start, 0))
    dist[start] = 0
    while pq:
        now, w = pq.pop(0)

        if dist[now] < w:
            continue
        dist[now] = w

        for next in graph[now]:
            next_v = next[0]
            next_w = next[1]

            if dist[next_v] <= next_w + w:
                continue

            dist[next_v] = next_w + w
            pq.append((next_v, next_w + w))



T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    INF = int(1e9)
    dist = [INF] * (N+1)
    dijkstra(0)
    result = dist[N]
    print(f'#{tc} {result}')