# 백준 3187. 양치기 꿍
import sys
from collections import deque
sys.stdin = open("bj3187input.txt")

def bfs(i, j):
    global result1, result2
    que = deque()
    que.append((i, j))
    visited[i][j] = 1

    cnt_1 = 0
    cnt_2 = 0
    if arr[i][j] == 'v':
        cnt_2 += 1
    elif arr[i][j] == 'k':
        cnt_1 += 1

    while que:
        y, x = que.popleft()
        for dy, dx in dir:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] != '#' and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                if arr[ny][nx] == 'v':
                    cnt_2 += 1
                elif arr[ny][nx] == 'k':
                    cnt_1 += 1
                que.append((ny, nx))

    if cnt_1 > cnt_2:
        result2 -= cnt_2
    else:
        result1 -= cnt_1


    return

# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N, M : 영역의 가로와 세로(3 <= R, C <= 250)
    N, M = map(int, input().split())

    '''
    arr[i][j] = . -> 빈 공간
    arr[i][j] = # -> 울타리
    arr[i][j] = v -> 늑대
    arr[i][j] = k -> 양
    울타리로 둘러싸이지 않은 곳에는 양과 늑대가 없음음
    울타리 안의 양 > 늑대 -> 늑대가 잡아먹힘
    울타리 안의 양 <= 늑대 -> 양이 잡아먹힘
    '''
    arr = [list(input()) for _ in range(N)]
    result1 = 0
    result2 = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'v':
                result2 += 1
            elif arr[i][j] == 'k':
                result1 += 1

    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            # 이미 방문한 테두리가 아니면서? 양 또는 늑대가 존재
            if visited[i][j] == 0 and arr[i][j] != '#':
                bfs(i, j)

    print(result1, result2)