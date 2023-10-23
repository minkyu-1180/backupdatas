# 백준 7568. 덩치
import sys
sys.stdin = open("bj7568input.txt")

# N : 전체 사람 수(2 <= N <= 50)
arr = []
N = int(input())
for i in range(N):
    arr.append(list(map(int, input().split())))
# print(arr)

# visited = [[0] * N for _ in range(N)]

result = [0] * N
for i in range(N-1):
    x1, y1 = arr[i]
    for j in range(i+1, N):
        x2, y2 = arr[j]
        # if visited[i][j] == 0:
        #     visited[i][j] = 1
        if x1 > x2 and y1 > y2:
            result[j] += 1
        elif x1 < x2 and y1 < y2:
            result[i] += 1

for num in result:
    print(num+1, end = ' ')
print()


