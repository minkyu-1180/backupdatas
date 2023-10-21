# 백준 1764. 듣보잡
import sys
sys.stdin = open("bj1764input.txt")

# N : 듣도못한 사람 수(1<= N <=500000)
# M : 보도못한 사람 수(1<= M <= 500000)
N, M = map(int, input().split())
set_N = set()
for _ in range(N):
    set_N.add(input())
set_M = set()
for _ in range(M):
    set_M.add(input())


result = sorted(list(set_N & set_M))
print(len(result))
for name in result:
    print(name)
