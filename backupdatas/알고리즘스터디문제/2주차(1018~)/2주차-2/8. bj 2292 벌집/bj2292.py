# 백준 2292. 벌집
import sys
sys.stdin = open("bj2292input.txt")

# 1 : 1개
# 2 3 4 5 6 7 : 6개
# 8 ~ 19 : 12개
# 20 ~ 37 : 18개
N = int(input())

num = 1
c = 1
while num < N:
    num += 6 * c
    c += 1
print(c)