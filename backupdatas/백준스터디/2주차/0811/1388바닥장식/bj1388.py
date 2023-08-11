# 백준 1388. 바닥 장식
import sys
sys.stdin = open("1388input.txt")
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    c = 0


    for i in range(N):
        stack = []
        for j in range(M-1):
            if arr[i][j] == '-':
                if arr[i][j+1] == '|':
                    c += 1
        if arr[i][M-1] == '-':
            c += 1

    for j in range(M):
        stack = []
        for i in range(N - 1):
            if arr[i][j] == '|':
                if arr[i + 1][j] == '-':
                    c += 1
        if arr[N - 1][j] == '|':
            c += 1
    print(c)
