# 백준 1931 회의실 배정
import sys
sys.stdin = open('1931input.txt')
from collections import deque

N = int(input())
# 각 원소 : (시작, 끝)
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key = lambda x : (x[1], x[0])) # s, e = 2, 2같은 상황 방지

c = 1
# 가장 일찍 끝나는 회의
end = arr[0][1]

for i in range(1, N):
    # 다음 회의 시작 시간이 현재 회의 끝 시간보다 빠르지 않을 때 -> 가능
    if arr[i][0] >= end:
        c += 1
        # 회의 끝 시간 갱신
        end = arr[i][1]
print(c)


