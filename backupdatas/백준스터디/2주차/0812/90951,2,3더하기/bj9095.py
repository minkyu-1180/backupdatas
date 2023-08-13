# 백준 9095. 1, 2, 3 더하기
import sys
sys.stdin = open("9095input.txt")

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    x, y, z = 1, 2, 4
    if n == 1:
        print(x)
    elif n == 2:
        print(y)
    elif n == 3:
        print(z)
    else:
        for _ in range(n-3):
            result = x + y + z
            x, y, z = y, z, result
        print(result)