# 백준 2622. 삼각형 만들기
import sys
sys.stdin = open("bj2622input.txt")
N = int(input())

result = 0
s = n_s = 0

if N == 1 or N == 2 or N == 4:
    result = 0
else:
    x = N//4
    if N%4 == 0:
        s = x - 1
        n_s = s - 1
    elif N%4 == 1:
        s = x
        n_s = s - 1
    elif N%4 == 2:
        s = x
        n_s = s - 2
    elif N%4 == 3:
        s = x + 1
        n_s = s - 2



    while s > 0:
        result += s
        if n_s > 0:
            result += n_s
        s -= 3
        n_s -= 3

print(result)

# else:
#     k = N//6
#     if N % 6 == 0:
#         for i in range(1, k):
#             result += ((3*k+i)//2 - (2*i-1))
#
#     elif N % 6 == 1:
#         for i in range(1, k+1):
#             result += ((3 * k + i) // 2 - (2 * (i - 1)))
#
#     elif N % 6 == 2:
#         for i in range(1, k+1):
#             result += ((3 * k + 1 + i) // 2 - (2 * i - 1))
#
#     elif N % 6 == 3:
#         for i in range(0, k+1):
#             result += ((3 * k + 2 + i) // 2 - (2 * i))
#
#     elif N % 6 == 4:
#         for i in range(1, k+1):
#             result += ((3 * k + 2 + i) // 2 - (2 * i - 1))
#         result += 1
#     elif N % 6 == 5:
#         for i in range(0, k + 1):
#             result += ((3 * k + 3 + i) // 2 - (2 * i))
#

print(result)


