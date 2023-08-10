# 가장 빠른 문자열 타이핑
import sys
sys.stdin = open("faststringtypinginput.txt")

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()

    N = len(A)
    M = len(B)

    i = 0
    j = 0
    counts = 0

    while j < M and i < N:
        if A[i] != B[j]:
            i = i - j
            j = - 1

        i = i + 1
        j = j + 1

        if j == M:
            j = 0
            counts += 1


    print(f'#{tc} {N - (M-1)*counts}')
