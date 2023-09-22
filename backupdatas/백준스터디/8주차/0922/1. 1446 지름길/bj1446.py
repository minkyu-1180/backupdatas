# 백준 1446. 지름길
import heapq
import sys
sys.stdin = open("bj1446input.txt")

def dijkstra(start):
    pq = []

    heapq.heappush(pq, (0, start))
    dist[start] = 0
    while pq:
        # node까지 가는 거리, 현재 노드
        w, node = heapq.heappop(pq)
        if node > D or dist[node] < w:
            continue
        dist[node] = w

        if node in graph.keys():
            for next_node, weight in graph[node]:
                if dist[next_node] < w + weight:
                    continue
                dist[next_node] = w + weight
                heapq.heappush(pq, (w+weight, next_node))

        heapq.heappush(pq, (w+1, node+1))




T = int(input())
for tc in range(T):
    N, D = map(int, input().split())
    # print(N, D)
    graph = dict()
    for _ in range(N):
        s, e, w = map(int, input().split())
        if e <= D and (e-s) > w:
            if s in graph.keys():
                graph[s].append((e, w))
            else:
                graph[s] = [(e, w)]
    # print(graph)
    dist = [i for i in range(0, D+1)]
    # print(len(dist))
    dijkstra(0)
    print(dist[D])
