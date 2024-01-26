# 백준 11060. 점프 점프
import sys
from collections import deque
sys.stdin = open("bj11060input.txt")

def bfs():
    que = deque()
    visited = [int(1e9)] * N
    que.append((0, 0))
    visited[0] = 0
    while que:
        now, c = que.popleft()
        if now == N-1:
            return c
        next = arr[now]
        for n in range(now+1, min(N, now+next+1)):
            if visited[n] <= c+1:
                continue
            que.append((n, c+1))
            visited[n] = c+1
    return -1
#
# N : 미로 칸 수(1 <= N <= 1000)
N = int(input())
# 재환이는 arr[0]에서 시작
arr = list(map(int, input().split()))

print(bfs())