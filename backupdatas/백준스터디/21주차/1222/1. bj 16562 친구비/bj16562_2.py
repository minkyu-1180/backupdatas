# 두 번쨰 풀이(heapq 사용)
import sys
sys.stdin = open("bj16562input.txt")
import heapq
from collections import deque

def bfs(std):
    global result
    que = deque()
    que.append(std)
    while que:
        now = que.popleft()
        for next in graph[now]:
            if visited[next]:
                continue
            visited[next] = 1
            que.append(next)



T = int(input())
for tc in range(T):
    N, M, k = map(int, input().split())
    arr = list(map(int, input().split()))

    pq = []
    # 요구하는 친구비가 작은 순으로 담기
    for i in range(N):
        heapq.heappush(pq, (arr[i], i))

    graph = [set() for _ in range(N)]
    for _ in range(M):
        v, w = map(int, input().split())
        if v != w:
            graph[v-1].add(w-1)
            graph[w-1].add(v-1)
    visited = [0] * N

    result = 0
    while pq:
        cost, std = heapq.heappop(pq)

        if visited[std]:
            continue
        visited[std] = 1
        result += cost
        bfs(std)
    # print(result)
    # print(visited)
    if result <= k:
        print(result)
    else:
        print("Oh no")