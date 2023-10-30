# 백준 13241. 최소공배수
import sys
sys.stdin = open("bj13241input.txt")
from math import lcm
# 원래 T는 없음
T = int(input())
for tc in range(T):
    a, b = map(int, input().split())
    print(lcm(a, b))