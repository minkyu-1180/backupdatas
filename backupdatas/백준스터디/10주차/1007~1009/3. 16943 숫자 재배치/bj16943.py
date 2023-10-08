# 백준 16943. 숫자 재배치
import sys
from itertools import permutations
sys.stdin = open("bj16943input.txt")

# T = int(input())
# for tc in range(T):
#
#     A, B = map(str, input().split())
#     B = int(B)
#     result = -1
#     arr = ["".join(i) for i in permutations(A)]
#     for num in arr:
#         if num[0] == '0':
#             continue
#         num = int(num)
#         if num < B:
#             result = max(result, num)
#     print(result)

def backtracking(c, num):
    global result

    if c == N:
        if len(str(num)) == N:
            if num < B and result < num:
                result = num
        return

    if num > B:
        return

    for i in range(N):
        a = int(arr[i])
        if visited[i] == 0:
            visited[i] = 1
            backtracking(c+1, num * 10 + a)
            visited[i] = 0


T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    arr = list(str(A))
    N = len(arr)
    visited = [0] * N
    result = -1


    backtracking(0, 0)
    print(result)