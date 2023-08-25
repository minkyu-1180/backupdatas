# IM 대비 6. 백준 2563 색종이
import sys
sys.stdin = open("2563색종이input.txt")

N = int(input())
arr = [[0] * 100 for _ in range(100)]
result = 0
for _ in range(N):
    x1, y1 = map(int, input().split())
    # 해당 idx에서 시작하는 색종이 칠하기
    for i in range(y1, y1+10):
        for j in range(x1, x1+10):
            # 아직 안칠해진 경우, 칠해준 후 count 추가
            if arr[i][j] == 0:
                arr[i][j] = 1
                result += 1
print(result)