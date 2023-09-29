# 백준 14465. 소가 길을 건너간 이유 5
import sys
sys.stdin = open("bj14465input.txt")
N, K, B = map(int, input().split())
arr = [0] * (N+1)
for _ in range(B):
    arr[int(input())] = 1
for i in range(1, N+1):
    arr[i] += arr[i-1] # 누적합
# arr[i] : i-(K-1) ~ i까지의 고쳐야 할 신호등 수
# arr[i] - arr[i-K] : ~i까지 연속된 K개의 신호등 중 고쳐야 할 신호등 개수
result = B
for i in range(K, N+1):
    if result > arr[i] - arr[i-K]:
        result = arr[i] - arr[i-K]
print(result)
# result = N
# for i in range(1, N-K+1):
#     if result > arr[i:i+K].count(1):
#         result = arr[i:i+K].count(1)
# print(result)


