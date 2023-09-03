# 백준 2531. 회전 초밥
import sys
from collections import deque
sys.stdin = open("bj2531input.txt")
T = int(input())
for test_case in range(T):
    '''
    N : 회전대에 올려져있는 초밥 개수
    d : 초밥의 가지 수
    k : 연속해서 먹을 초밥 수
    c : 쿠폰 번호    
    '''
    N, d, k, c = map(int, input().split())
    arr = list(int(input()) for _ in range(N))
    result = 0


    for i in range(N):
        left, right = i, i+k
        if right > N:
            types = set(arr[left:N] + arr[:right%N])
        else:
            types = set(arr[left:right])
        types.add(c)
        result = max(result, len(types))

    print(result)








