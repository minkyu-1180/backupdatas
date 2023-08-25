# IM 대비 7. 백준 2567 색종이2
import sys
sys.stdin = open("2567색종이2input.txt")

N = int(input()) # 색종이 수(<= 100)
arr = [[0] * 102 for _ in range(102)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            arr[i][j] = 1
result = 0
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for i in range(1, 101):
    for j in range(1, 101):
        if arr[i][j] == 1:
            for di, dj in dir:
                ni = i + di
                nj = j + dj
                if arr[ni][nj] == 0:
                    result += 1


print(result)