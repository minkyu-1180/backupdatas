# 백준 1427. 소트인사이드
import sys
sys.stdin = open("bj1427input.txt")

# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N : 정렬하려고 하는 수
    # 1 <= N <= 1000000000
    # N의 각 자리수의 값들을 원소로 하는 배열 생성
    N = list(map(str, input()))
    N.sort(reverse=True)
    print("".join(N))
