# 5789. 현주의 상자 바꾸기

import sys
sys.stdin = open("boxchangeinput.txt")

T = int(input())
for test_case in range(1, T + 1):
    N, Q = map(int, input().split())
    arr = [0] * (N + 1)
    # arr = [0, 0, 0, ,,, 0]
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            arr[j] = i
    popzero = arr.pop(0)

    print(f'#{test_case}', end = ' ')
    for i in range(N-1):
        print(arr[i], end = ' ')
    print(arr[N-1])

    '''
    [0, 0, 0, 0, 0]
    i = 1, L = 1, R = 3
    [1, 1, 1, 0, 0]
    '''