'''import sys
sys.stdin = open("miroinput.txt")
T = int(input())
for test_case in range(1, T+1):
    # 5 <= N <= 100
    N = int(input())
    arr = [input() for _ in range(N)]
    start = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                start.append(i)
                start.append(j)
    # [i,j]
    print(start)
    result = 0
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    while True:
        i = start[0]
        j = start[1]

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == '3':
                    result = 1
                    break
                elif arr[ni][nj] == '0':
                    start[0] = ni
                    start[1] = nj
                    break
'''
import sys
sys.stdin = open("miroinput.txt")
T = int(input())
for test_case in range(1, T+1):
    # 5 <= N <= 100
    N = int(input())
    arr = [input() for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    start_i = 0
    start_j = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                start_i, start_j = i, j
    result = 0
    stack = []
    i = start_i
    j = start_j
    while True:
        visited[i][j] = 1

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0 and arr[ni][nj] != '1':
                    stack.append([i, j])
                    i = ni
                    j = nj
                    visited[i][j] = 1
                    break
        else:
            if stack:
                i, j = stack.pop()
            else:
                break
        if arr[i][j] == '3':
            result = 1
            break
    print(f'#{test_case} {result}')
