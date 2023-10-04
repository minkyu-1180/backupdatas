# 백준 15903. 카드 합체 놀이

import sys
sys.stdin = open("bj15903input.txt")
import heapq

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    c = 0
    result = sum(arr)
    while c < M:
        num1 = heapq.heappop(arr)
        num2 = heapq.heappop(arr)
        heapq.heappush(arr, num1+num2)
        heapq.heappush(arr, num1+num2)
        result += num1+num2
        c += 1
    print(result)
