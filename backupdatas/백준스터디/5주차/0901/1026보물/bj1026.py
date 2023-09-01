# 백준 1026. 보물
import sys
sys.stdin = open("1026input.txt")

T = int(input())
for test_case in range(1, T+1):
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = 0
for _ in range(N):
    result += A.pop(A.index(max(A))) * B.pop(B.index(min(B)))
print(result)