# 1952. 달팽이2
import sys
sys.stdin = open("1952input.txt")

N, M = map(int, input().split())
arr = [[0]*M for _ in range(N)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
count = -1
n = 1
i = j = 0
k = 0
while n <= N * M:
    arr[i][j] = n
    ni = i + di[k]
    nj = j + dj[k]
    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
        i = ni
        j = nj
    else:
        k = (k + 1) % 4
        i, j = i + di[k], j + dj[k]
        count += 1
    n += 1

print(count)




