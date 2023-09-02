# # 백준 10819. 차이를 최대로
import sys
sys.stdin = open("bj10819input.txt")

def func(idx):
    global result
    if idx == N:
        c = 0
        for i in range(N-1):
            c += abs(p[i] - p[i+1])
        if result < c:
            result = c

    for i in range(N):
        if visited[i] == 0:
            p.append(arr[i])
            visited[i] = 1
            func(idx+1)
            visited[i] = 0
            p.pop()

N = int(input())
arr = list(map(int, input().split()))
result = 0
visited = [0] * N
p = []
func(0)
print(result)