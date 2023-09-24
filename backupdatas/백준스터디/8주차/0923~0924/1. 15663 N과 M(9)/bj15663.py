# 백준 15663. N과 M(9)
import sys
sys.stdin = open("bj15663input.txt")

def backtracking(c, lst):
    if c == M:
        print(*lst)
        return
    last = 0
    for i in range(N):
        if visited[i] == 0 and last != arr[i]:
            visited[i] = 1
            lst.append(arr[i])
            last = arr[i]
            backtracking(c+1, lst)
            visited[i] = 0
            lst.pop()

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    visited = [0] * N
    lst = []

    backtracking(0, lst)