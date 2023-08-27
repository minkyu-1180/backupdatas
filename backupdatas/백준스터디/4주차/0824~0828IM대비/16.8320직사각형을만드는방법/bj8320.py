# IM 대비 16. 백준 8320 직사각형을 만드는 방법
import sys
sys.stdin = open('8320직사각형input.txt')

N = int(input())

# 높이 : a
# a <= b의 구조
a = 1
result = 0
while (a**2) <= N:
    for b in range(a, N+1):
        if a * b <= N:
            result += 1

    a += 1
print(result)