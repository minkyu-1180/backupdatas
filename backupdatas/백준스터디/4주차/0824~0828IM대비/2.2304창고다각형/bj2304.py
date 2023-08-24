# IM 대비 2. 백준 2304 창고 다각형
import sys
sys.stdin = open("2304창고다각형input.txt")

N = int(input()) # 기둥의 개수 (1 <= N <= 1000)
arr = [0] * 1001
max_l = 0 # 가장 끝 idx
max_i = 0 # 가장 높은 기둥을 가진 idx
for _ in range(N):
    # L : 기둥 왼쪽 위치(idx)
    # H : 기둥 높이
    # 1 ~ 1000
    L, H = map(int, input().split())
    arr[L] = H
    if max_l < L:
        max_l = L
    if arr[max_i] < H:
        max_i = L



# 1. 가장 높은 기둥을 가진 idx기준 왼쪽(1 ~ max_i-1)
result = 0
max_v1 = 0
for i in range(1, max_i):
    if max_v1 < arr[i]:
        max_v1 = arr[i]
    result += max_v1

# 2. 가장 높은 기둥을 가진 idx 기준 오른쪽(max_i + 1 ~ max_l)
max_v2 = 0
for i in range(max_l, max_i, -1):
    if max_v2 < arr[i]:
        max_v2 = arr[i]
    result += max_v2
# 3. 가장 높은 기둥
result += arr[max_i]

print(result)


