# 백준 11650. 좌표 정렬하기
import sys
sys.stdin = open("bj11650input.txt")

# N : 점의 개수(1<=N<=100000)
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr.sort()
for x, y in arr:
    print(x, y)