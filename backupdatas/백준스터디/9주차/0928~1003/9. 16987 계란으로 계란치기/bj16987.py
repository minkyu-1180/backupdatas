# 백준 16987. 계란으로 계란치기
import sys
sys.stdin = open("bj16987input.txt")

def broken_eggs(arr):
    result = 0
    for s, w in arr:
        if s <= 0:
            result += 1
    return result

def backtracking(idx):
    global result

    if idx == N:
        result = max(result, broken_eggs(arr))
        return

    if arr[idx][0] <= 0:
        backtracking(idx+1)
    else:
        for i in range(N):
            if i != idx and arr[i][0] > 0:
                s1, w1 = arr[idx]
                s2, w2 = arr[i]
                arr[idx] = [s1-w2, w1]
                arr[i] = [s2-w1, w2]
                backtracking(idx+1)
                arr[idx] = [s1, w1]
                arr[i] = [s2, w2]

        else:
            backtracking(N)

T = int(input())
for tc in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    result = 0
    backtracking(0)
    print(result)