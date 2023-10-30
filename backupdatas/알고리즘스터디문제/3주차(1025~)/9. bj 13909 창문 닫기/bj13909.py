# 백준 13909. 창문 닫기
import sys
sys.stdin = open("bj13909input.txt")


# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N : 창문 개수 & 사람의 수(1<=N<=2100000000)
    N = int(input())
    result = int(N**(0.5))
    print(result)