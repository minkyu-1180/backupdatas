# sw academy 미로2
import sys
sys.stdin = open("미로2input.txt")

def bfs(start):
    queue = []
    visited = [[0] * 100 for _ in range(100)]

    queue.append(start)
    visited[start[0]][start[1]] = 1

    while queue:
        node = queue.pop(0)
        i, j = node[0], node[1]
        if arr[i][j] == 3:
            return 1
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < 100 and 0 <= nj < 100 and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                node = [ni, nj]
                queue.append(node)
                visited[ni][nj] = 1
    return 0


for test_case in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(100)]

    start = [1, 1]
    result = bfs(start)
    print(f'#{test_case} {result}')