# 종이 붙이기
import sys
sys.stdin = open("paperinput.txt")

#
def Factorial(n):
    if n == 1:
        return 1
    else:
        return n * Factorial(n-1)

# nCr = n!/(r! * (n-r)!)
def Combination(n, r):
    return (Factorial(n)) / (Factorial(r) * Factorial(n-r))

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    result = 0
    for y in range(N//2, -1, -1):
        x = N - 2*y
        result *= Combination(x+y, y)
        result *= 2 ** y
        print(result)
