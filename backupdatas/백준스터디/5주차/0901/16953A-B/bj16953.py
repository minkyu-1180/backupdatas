# 백준 16953. A -> B
import sys
sys.stdin = open("16953input.txt")


def atob(A, B, c):
    global min_c
    if A == B:
        if min_c > c:
            min_c = c
    elif A < B:
        atob(A*2, B, c+1)
        atob(A*10 + 1, B, c+1)



T = int(input())
for test_case in range(1, T+1):
    A, B = map(int, input().split())
    min_c = B
    atob(A, B, 0)

    if min_c == B-A:
        print(-1)
    else:
        print(min_c+1)


