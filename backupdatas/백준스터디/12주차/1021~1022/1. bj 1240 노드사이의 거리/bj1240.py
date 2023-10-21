# 백준 1240. 노드사이의 거리
import sys
from collections import deque
sys.stdin = open("bj1240input.txt")

def dfs(s, d):
    global result

    if s == e:
        result = d
        return

    for next, dist in tree[s]:
        if visited[next] == 0:
            visited[next] = 1
            dfs(next, d+dist)


N, M = map(int, input().split())
tree = [[] for _ in range(N+1)]
# 본인 자식
for _ in range(N-1):
    s, e, dist = map(int, input().split())
    tree[s].append((e, dist))
    tree[e].append((s, dist))
# print(tree)
for _ in range(M):
    s, e = map(int, input().split())
    result = 0
    visited = [0] * (N+1)
    visited[s] = 1
    dfs(s, 0)
    print(result)
