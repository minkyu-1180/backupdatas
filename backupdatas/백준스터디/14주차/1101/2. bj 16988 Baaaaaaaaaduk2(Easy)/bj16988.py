# 백준 16988. Baaaaaaaaaduk2(Easy)
import sys
sys.stdin = open("bj16988input.txt")

# 원래 T는 없음
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
