# 백준 2841. 외계인의 기타 연주
import sys
sys.stdin = open("bj2841input.txt")
T = int(input())
for tc in range(T):
    N, P = map(int, input().split())
    result = 0
    arr = [[] for _ in range(7)]

    for i in range(N):
        n, p = map(int, sys.stdin.readline().split())
        if not arr[n]:
            arr[n].append(p)
            result += 1
        else:
            while arr[n] and arr[n][-1] > p:
                arr[n].pop()
                result += 1
            if arr[n] == [] or arr[n][-1] < p:
                arr[n].append(p)
                result += 1

    print(result)



