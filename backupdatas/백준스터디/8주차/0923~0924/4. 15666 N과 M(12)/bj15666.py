# 백준 15666. N과 M(12)
import sys
sys.stdin = open("bj15666input.txt")

def backtracking(c, lst, last):
    if c == M:
        print(*lst)
        return

    for i in range(last, len(arr)):
        if last <= arr[i]:
            lst.append(arr[i])
            last = arr[i]
            backtracking(c+1, lst, i)
            lst.pop()

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = list(set(arr))
    arr.sort()

    backtracking(0, [], 0)