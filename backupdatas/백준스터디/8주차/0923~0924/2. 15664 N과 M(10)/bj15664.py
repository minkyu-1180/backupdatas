# 백준 15664. N과 M(10)
import sys
sys.stdin = open("b15664jinput.txt")

def backtracking(c, idx, lst):
    if c == M:
        print(*lst)
        return

    last = 0
    for i in range(idx, N):
        if visited[i] == 0 and last != arr[i]:
            visited[i] = 1
            lst.append(arr[i])
            last = arr[i]
            backtracking(c+1, i+1, lst)
            visited[i] = 0
            lst.pop()




T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    visited = [0] * N
    lst = []

    backtracking(0, 0, lst)
