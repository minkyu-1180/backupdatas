# 백준 17129. 윌리암슨수액빨이딱따구리가 정보섬에 올라온 이유
import sys
from collections import deque
sys.stdin = open("bj17129input.txt")

def bfs():
    global result1, result2

    while que:
        i, j = que.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                que.append([ni, nj])
                visited[ni][nj] = visited[i][j] + 1
                if arr[ni][nj] in (3, 4, 5):
                    result1 = 'TAK'
                    result2 = visited[ni][nj] - 1
                    return
    return


N, M = map(int, input().split())
arr = []
idx_2 = (0, 0)
for i in range(N):
    lst = list(map(int, input()))
    if 2 in lst:
        j = lst.index(2)
        idx_2 = (i, j)
        lst[j] = 1
    arr.append(lst)


visited = [[0]*M for _ in range(N)]
que = deque()
i, j = idx_2
que.append([i, j])
visited[i][j] = 1

di = [0, 0, -1, 1]
dj = [1,-1, 0, 0]

result1 = 'NIE'
result2 = 0
bfs()
if result2 == 0:
    print(result1)
else:
    print(result1)
    print(result2)