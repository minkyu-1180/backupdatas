# 백준 11399. ATM
import sys
sys.stdin = open("bj11399input.txt")
# N : 사람 수(1<=N<=1000)
N = int(input())
# arr[i] : i+1번 사람이 돈을 인출하는데 걸리는 시간
arr = list(map(int, input().split()))
arr.sort()
result = 0
for i in range(N):
    for j in range(i+1):
        result += arr[j]
print(result)