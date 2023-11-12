# 백준 1037. 약수
import sys
sys.stdin = open("bj1037input.txt")

# 원래 T는 없음
T = int(input())
for tc in range(T):
    # K : N의 진짜 약수(1, N을 제외한 약수)
    K = int(input())
    # N의 진짜 약수들
    arr = list(map(int, input().split()))
    arr.sort()
    N = arr[0] * arr[K-1]
    print(N)