# sw academy 미로1
import sys
sys.stdin = open("미로1input.txt")

def bfs(start):
    queue = []
    visited = [[0] * 16 for _ in range(16)]

    queue.append(start)
    visited[start[0]][start[1]] = 1

    while queue:
        node = queue.pop(0)
        j, i = node[1], node[0]
        if arr[i][j] == 3:
            return 1
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < 16 and 0 <= nj < 16 and arr[ni][nj] != 1 and visited[ni][nj] == 0 :
                queue.append([ni, nj])
                visited[ni][nj] = 1
    return 0


for test_case in range(1, 11):
    tc = int(input())
    # 미로(16 X 16)
    # 우리가 볼 곳 : (1, 1) ~ (13, 13) -> range(1, 14)
    # i or j = 0 -> 무조건 1
    # 미로의 시작점(2인 idx) : (1, 1)
    # 미로의 도착점 : 3인 idx
    arr = [list(map(int, input())) for _ in range(16)]
    start = [1, 1]
    print(f'#{test_case} {bfs(start)}')






