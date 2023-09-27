# 백준 1325. 효율적인 해킹
import sys
from collections import deque

def bfs(i):
    visited = [0] * (N+1)
    visited[i] = 1
    que = deque()
    que.append(i)
    c = 1
    while que:
        now = que.popleft()
        if graph[now]:
            for next in graph[now]:
                if visited[next] == 0:
                    visited[next] =1
                    que.append(next)
                    c += 1
    return c


sys.stdin = open("bj1325input.txt")
N, M = map(int, input().split())

graph = [set() for _ in range(N+1)]
parent = [i for i in range(N+1)]
hacking_num = [0] * (N+1)
for _ in range(M):
    # A가 B를 신뢰한다
    # B를 해킹하면, A도 해킹 가능하다
    A, B = map(int, input().split())
    graph[B].append(A)

for i in range(1, N+1):
    c = bfs(i)
    hacking_num[i] = c

max_c = max(hacking_num)
for i in range(1, N+1):
    if hacking_num[i] == max_c:
        print(i, end = ' ')
print()
