# 백준 2210. 숫자판 점프
import sys
from collections import deque
sys.stdin = open("bj2210input.txt")


# def bfs(i, j, string):
#     que = deque()
#     que.append((i, j, string))
#     visited[i][j] = 1
#
#     while que:
#         i, j, string = que.popleft()
#         if len(string) == 6:
#             result.add(string)
#
#         for di, dj in dir:
#             ni = i + di
#             nj = j + dj
#             if 0 <= ni < 5 and 0 <= nj < 5 and visited[ni][nj] == 0:
#                 visited[ni][nj] = 1
#                 que.append((ni, nj, string+arr[ni][nj]))



def backtracking(i, j, c, string):
    if c == 6:
        result.add(string)
        return

    for di, dj in dir:
        ni = i + di
        nj = j + dj
        if 0 <= ni < 5 and 0 <= nj < 5:
            backtracking(ni, nj, c+1, string+arr[ni][nj])




arr = [list(map(str, input().split())) for _ in range(5)]
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

result = set()
for i in range(5):
    for j in range(5):
        string = arr[i][j]
        backtracking(i, j, 1, string)
print(len(result))