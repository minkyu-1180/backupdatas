# 백준 1158. 요세푸스
import sys
sys.stdin = open("1158input.txt")

# N과 K 입력
N, K = map(int, input().split())

arr = list(range(1, N+1))
result = []
jump = K-1
idx = 0
for i in range(N):
    idx += jump
    # jump후 인덱스가 벗어난 경우
    if idx >= len(arr):
        idx = idx % len(arr)
    result.append(arr[idx])
    arr.pop(idx)

print('<', end = '')
for i in range(N-1):
    print(result[i], end = ', ')
print(f'{result[-1]}>')




