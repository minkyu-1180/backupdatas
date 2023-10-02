# 백준 10166. 관중석
import sys
from math import gcd
sys.stdin = open("bj10166input.txt")
def GCD(i, j):
    num = min(i, j)
    for n in range(num, 0, -1):
        i_rest = i%n
        j_rest = j%n
        if i_rest == j_rest == 0:
            return n


def greatest_common_divisor(D1, D2):
    global result
    for i in range(D1, D2 + 1):
        for j in range(1, i + 1):
            g = GCD(i, j)
            if arr[i//g][j//g] == 0:
                arr[i//g][j//g] = 1
                result += 1
    return result


D1, D2 = map(int, input().split())
arr = [[0] * 2001 for _ in range(2001)]
result = 0
greatest_common_divisor(D1, D2)
print(result)