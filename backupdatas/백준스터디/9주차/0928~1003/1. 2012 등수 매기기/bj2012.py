# 백준 2012. 등수 매기기
import sys
sys.stdin = open("bj2012input.txt")

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()
result = 0
for i in range(1, N+1):
    result += abs(i-arr[i-1])
print(result)

