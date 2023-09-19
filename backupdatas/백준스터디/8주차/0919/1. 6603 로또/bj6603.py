# 백준 6603. 로또
import sys
sys.stdin = open("bj6603input.txt")

def backtracking(idx):
    if idx == 7:
        for i in range(1, 7):
            print(visited[i], end = ' ')
        print()
        return

    for i in range(N):
        if arr[i] > visited[idx-1]:
            visited[idx] = arr[i]
            backtracking(idx+1)
            visited[idx] = 0



lst = list(map(int, input().split()))
while True:
    k = lst[0]
    arr = lst[1:]
    if k == 0:
        break

    N = len(arr)
    result = []
    visited = [0] * 7
    backtracking(1)

    print()
    lst = list(map(int, input().split()))
