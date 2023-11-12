import sys
sys.stdin = open("bj15439input.txt")
# 원래 T는 없음
T = int(input())
for tc in range(T):
    n = int(input())
    print(n * (n - 1))