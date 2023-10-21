# 백준 1620. 나는야 포켓몬 마스터 이다솜
import sys
from collections import defaultdict
sys.stdin = open("bj1620input.txt")

# N : 도감에 수록되어있는 포켓몬의 개수(1 <= N <= 100000)
# M : 내가 맞춰야 하는 문제 개수(1 <= M <= 100000)
N, M = map(int, input().split())

pocketmons = {}

for i in range(1, N + 1):
    pocketmon = input().rstrip()
    pocketmons[i] = pocketmon
    pocketmons[pocketmon] = i

for i in range(M):
    pocketmon = input().rstrip()
    if pocketmon.isdigit():
        print(pocketmons[int(pocketmon)])
    else:
        print(pocketmons[pocketmon])