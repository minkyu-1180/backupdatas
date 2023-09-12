# 백준 13549. 숨바꼭질 3
from collections import deque
import sys
sys.stdin = open("bj13549input.txt")
# sys.setrecursionlimit()

'''
def bfs(N, K, t):
    global result
    if K == N:
        if result > t:
            result = t
            return

    if t < result:
        if K % 2 == 0 and K > N:
            bfs(N, K//2, t)
        bfs(N, K+1, t+1)
        bfs(N, K-1, t+1)
'''

# result = 100000
# if N >= K:
#     result = N-K
# else:
#     bfs(N, K, 0)


from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

que = deque()
que.append(N)

visited = [0] * 100001
visited[N] = 1

while que:
    now = que.popleft()
    if 0 < now * 2 <= 100000 and visited[now * 2] == 0:
        que.appendleft(now * 2)
        visited[now * 2] = visited[now]
    if 0 <= now - 1  and visited[now - 1] == 0:
        que.append(now - 1)
        visited[now - 1] = visited[now] + 1
    if now + 1 <= 100000 and visited[now + 1] == 0:
        que.append(now + 1)
        visited[now + 1] = visited[now] + 1

    if visited[K]:
        print(visited[K]-1)
        break


