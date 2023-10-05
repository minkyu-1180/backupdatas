# 백준 1074. Z
import sys
sys.stdin = open("bj1074input.txt")
sys.setrecursionlimit(10**6)
def backtracking(i, j, n, val):
    if n == 1:
        arr[0][0] = val
        arr[0][1] = val+1
        arr[1][0] = val+2
        arr[1][1] = val+3
        print(arr[r-i][c-j])
        return

    if i <= r < i+2**(n-1) and j <= c < j+2**(n-1):
        backtracking(i, j, n-1, val)
    elif i <= r < i+2**(n-1) and j+2**(n-1) <= c < j+2**n:
        backtracking(i, j+2**(n-1), n-1, val+2**(2*(n-1)))
    elif i+2**(n-1) <= r < i+2**n and j <= c < j+2**(n-1):
        backtracking(i+2**(n-1), j, n-1, val+2 * 2**(2*(n-1)))
    elif i+2**(n-1) <= r < i+2**n and j+2**(n-1) <= c < j+2**n:
        backtracking(i+2**(n-1), j+2**(n-1), n-1, val+3 * 2**(2*(n-1)))




T = int(input())
for tc in range(T):
    N, r, c = map(int, input().split())
    arr = [[0, 0], [0, 0]]
    backtracking(0, 0, N, 0)

