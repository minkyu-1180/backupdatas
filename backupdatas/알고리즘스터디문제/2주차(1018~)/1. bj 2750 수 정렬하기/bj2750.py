# 백준 2750. 수 정렬하기
import sys
sys.stdin = open("bj2750input.txt")
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
for num in sorted(arr):
    print(num)