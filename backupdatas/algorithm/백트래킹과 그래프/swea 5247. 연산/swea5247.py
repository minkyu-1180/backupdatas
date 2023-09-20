# swea 5247. 연산
import sys
from collections import deque
sys.stdin = open("swea5247input.txt")

def bfs():
    while que:
        now = que.popleft()
        if now == M:
            return visited[now]

        if now*2 <= 1000000 and visited[now*2] == -1:
            que.append(now*2)
            visited[now*2] = visited[now] + 1

        if now-10 <= 1000000 and visited[now-10] == -1:
            que.append(now-10)
            visited[now-10] = visited[now] + 1

        if now+1 <= 1000000 and visited[now+1] == -1:
            que.append(now+1)
            visited[now+1] = visited[now] + 1

        if 1 <= now-1 and visited[now-1] == -1:
            que.append(now-1)
            visited[now-1] = visited[now] + 1



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [-1] * 1000001
    visited[N] = 0
    que = deque()
    que.append(N)
    result = bfs()

    print(f'#{tc} {result}')