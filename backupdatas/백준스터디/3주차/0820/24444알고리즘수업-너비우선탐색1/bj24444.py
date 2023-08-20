# 백준 24444. 알고리즘 수업 - 너비 우선 탐색 1
import sys
sys.stdin = open('24444input.txt')
from collections import deque

def BFS(adj, start):
    global c
    queue = deque([])
    queue.append(start)
    visited[start] = c

    while queue:
        start = queue.popleft()
        for next in adj[start]:
            if visited[next] == 0:
                c += 1
                queue.append(next)
                visited[next] = c


N, M, R = map(int, input().split())

adj = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)
for nodes in adj:
    nodes.sort()

visited = [0] * (N+1)
c = 1

BFS(adj, R)

for i in range(1, N+1):
    print(visited[i])
