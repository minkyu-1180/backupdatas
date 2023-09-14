# 백준 2668. 숫자고르기
import sys
sys.stdin = open("bj2668input.txt")
N = int(input())
arr = [[0] * (N+1) for _ in range(2)]
for j in range(1, N+1):
    arr[0][j] = j
    arr[1][j] = int(input())
print(arr)




start, next = arr[0][1], arr[1][1]
visited = [[0] * (N+1) for _ in range(N+1)]
visited[start][next] = 1
stack = []

while True:
    start = next
    next = arr[1][start]
    # 돌고돌아 도착
    if visited[start][next] == 1:




