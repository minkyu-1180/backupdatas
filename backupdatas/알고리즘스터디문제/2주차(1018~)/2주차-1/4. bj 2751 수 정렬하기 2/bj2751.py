# 백준 2751. 수 정렬하기 2
import sys
sys.stdin = open("bj2751input.txt")

# N : 수의 개수(1<=N<=1000000)
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
for num in arr:
    print(num)