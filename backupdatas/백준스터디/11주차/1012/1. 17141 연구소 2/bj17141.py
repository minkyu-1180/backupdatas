# 백준 17141. 연구소 2
import sys
from itertools import combinations
from collections import deque
sys.stdin = open("bj17141input.txt")

def bfs(y, x):
    visited[y][x] = 0
    que = deque()
    que.append([y, x])

    while que:
        i, j = que.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and visited[ni][nj] > visited[i][j] + 1:
                visited[ni][nj] = visited[i][j]+1
                que.append([ni, nj])

# def check(visited):
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] != 1:
#                 if visited[i][j] == int(1e9):
#                     return False
#     return True



T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    viruses = []
    arr = []
    for i in range(N):
        lst = list(map(int, input().split()))
        arr.append(lst)
        for j in range(N):
            if arr[i][j] == 2:
                viruses.append((i, j))
    # for lst in arr:
        # print(lst)
    result = int(1e9)
    # 한 가지 경우라도 가능하면 True로 변환
    # is_possible = False
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    for case in combinations(viruses, M):
        # print(f'case : {list(case)}')
        visited = [[int(1e9)] * N for _ in range(N)]
        for y, x in case:
            # print(y, x)
            bfs(y, x)
        # for lst in visited:
        #     print(lst)
        # print()
        max_dist = 0
        for i in range(N):
            for j in range(N):
                if arr[i][j] != 1 and max_dist < visited[i][j]:
                    max_dist = visited[i][j]
        # print(max_dist)
        result = min(result, max_dist)
    # print(result)
    if result == int(1e9):
        print(-1)
    else:
        print(result)

