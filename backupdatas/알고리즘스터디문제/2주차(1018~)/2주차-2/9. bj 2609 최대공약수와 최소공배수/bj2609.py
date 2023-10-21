# 백준 2609. 최대공약수와 최소공배수
import sys
from math import gcd, lcm
sys.stdin = open("bj2609input.txt")

N, M = map(int, input().split())
print(gcd(N, M))
print(lcm(N, M))