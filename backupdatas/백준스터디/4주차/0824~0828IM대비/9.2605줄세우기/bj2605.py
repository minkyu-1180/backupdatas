# IM 대비 9. 백준 2605 줄세우기
import sys
sys.stdin = open("2605줄세우기input.txt")

N = int(input())
arr = [0] + list(map(int, input().split()))

result = [0] * (N+1)

for i in range(1, N+1):
    if arr[i] == 0:
        result[i] = i
    else:
        k = arr[i]
        result.insert(i-k, i)

for i in range(1, N+1):
    print(result[i], end = ' ')
print()