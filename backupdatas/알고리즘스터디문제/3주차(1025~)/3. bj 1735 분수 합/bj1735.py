# 백준 1735. 분수 합
import sys
sys.stdin = open("bj1735input.txt")
from math import gcd, lcm
a, b = map(int, input().split())
c, d = map(int, input().split())

Y = lcm(b, d)
X = (Y//b) * a + (Y//d) * c
# print((Y//b) * a)
# print((Y//d) * c)
num = gcd(X, Y)

print(X//num, Y//num)