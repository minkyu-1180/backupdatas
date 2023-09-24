# 백준 15665. N과 M(11)
import sys
sys.stdin = open("bj15665input.txt")

def backtracking(c, lst):
    if c == M:
        print(*lst)
        return

    for i in range(len(arr)):
        lst.append(arr[i])
        backtracking(c+1, lst)
        lst.pop()

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    arr = list(set(arr))
    arr.sort()
    backtracking(0, [])
