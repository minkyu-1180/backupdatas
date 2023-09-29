# 백준 1780. 종이의 개수
import sys
from collections import deque
sys.stdin = open("bj1780input.txt")

# def check(y, x, num, size):
#     for i in range(y, y+size):
#         for j in range(x, x+size):
#             if arr[i][j] != num:
#                 return False
#
#     return True
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# result = [0] * 3
# que = deque()
# que.append((0, 0, arr[0][0], N))
#
# while que:
#     y, x, num, size = que.popleft()
#     if check(y, x, num, size):
#         result[num+1] += 1
#     else:
#         size = size//3
#         if size:
#             for i in range(y, y + size * 3, size):
#                 for j in range(x, x + size * 3, size):
#                     que.append((i, j, arr[i][j], size))
#
# for num in result:
#     print(num)

def divide_conquer(y, x, num, size):
    for i in range(y, y+size):
        for j in range(x, x+size):
            if arr[i][j] != num:
                if size//3:
                    for k in range(y, y+size, size//3):
                        for l in range(x, x+size, size//3):
                            divide_conquer(k, l, arr[k][l], size//3)
                return
    result[num+1] += 1



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = [0] * 3
divide_conquer(0, 0, arr[0][0], N)
for num in result:
    print(num)