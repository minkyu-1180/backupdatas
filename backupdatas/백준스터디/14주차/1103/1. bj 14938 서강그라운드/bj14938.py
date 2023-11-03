# 백준 14938. 서강그라운드
import sys
sys.stdin = open("bj14938input.txt")
from collections import deque

def bfs(i):
    c = arr[i] # 시작 위치에서의 템 개수 포함
    visited = [0] * (N+1)
    visited[i] = 1

    que = deque()
    que.append((i, 0)) # 현재 간 거리
    while que:
        node, dist = que.popleft()
        for next, l in adj[node]:
            if visited[next] == 0 and dist + l <= M:
                visited[next] = 1
                que.append((next, dist+l))
                c += arr[next] # 템 개수 추가
    # i번 위치에서 시작했을 때 얻을 수 있는 템 개수 반환
    return c

import heapq
def dijkstra(i):
    c = 0
    pq = []
    dist = [M+1] * (N+1)
    # i를 시작점으로 했을 때, M의 거리 내로 갈 수 있는 지점들을 체크하는 visited 배열
    visited = [0] * (N+1)

    # 출발점과 거리 넣기
    heapq.heappush(pq, (0, i)) # 최초 dist, node 삽입
    # dist 표시 및 방문 여부 표시
    dist[i] = 0
    visited[i] = 1
    c += arr[i]
    while pq:
        d, node = heapq.heappop(pq)

        # 이미 더 짧은 거리로 간 경험이 있음 -> 넘기기
        if dist[node] < d:
            continue
        # 더 짧게 갈 수 있는 경우 -> 다음 지점 찾아보기
        for next, l in adj[node]:
            # 지금까지 걸어온 거리(d)에 다음 지점까지 가는 거리(l)의 합이 M이내일 경우
            if d + l <= M:
                # 다음 지점까지 가는 거리를 갱신 가능할 경우 -> heapq에 추가
                if dist[next] > d+l:
                    dist[next] = d+l
                    heapq.heappush(pq, (d+l, next))
                    # 만약 방문처리가 안된 경우, 방문 처리 및 아이템 개수 늘리기
                    if visited[next] == 0:
                        visited[next] = 1
                        c += arr[next]

    # print(dist)
    return c



# N : 지역의 개수(1 <= N <= 100)
# M : 예은이의 수색 범위(1 <= M <= 15)
# R : 길의 개수 (1 <= R <= 100)
N, M, R = map(int, input().split())
# arr[i] : i번 지역에 있는 아이템의 수(1 <= arr[i] <= 30)
arr = [0] + list(map(int, input().split()))

adj = [[] for _ in range(N+1)]
for _ in range(R):
    a, b, l = map(int, input().split())
    adj[a].append((b, l))
    adj[b].append((a, l))
# print(adj)
result = 0
for i in range(1, N+1):
    # print(dijkstra(i))
    result = max(result, dijkstra(i))
print(result)