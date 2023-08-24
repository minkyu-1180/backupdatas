# IM 대비 1. 백준 1063 킹
import sys
sys.stdin = open("1063킹input.txt")

T = int(input())
commands = {'R' : [0, 1],
       'L' : [0, -1],
       'B' : [-1, 0],
       'T' : [1, 0],
       'RT' : [1, 1],
       'LT' : [1, -1],
       'RB' : [-1, 1],
       'LB' : [-1, -1]
       }

for test_case in range(1, T+1):
    # 킹의 위치 / 돌의 위치 / 시행 횟수
    # king과 stone의 0번 : x좌표 / 1번 : y좌표

    king, stone, N = map(str, input().split())
    lst = [[0] * 9 for _ in range(9)]
    k_j, k_i = ord(king[0]) - 64, int(king[1])
    s_j, s_i = ord(stone[0]) - 64, int(stone[1])
    lst[k_i][k_j] = 1 # king은 1로 표현
    lst[s_i][s_j] = 2 # stone은 2로 표현

    # 주어진 명령에 반응하는 방법
    for _ in range(int(N)):
        cmd = input()
        direct = commands[cmd]
        k_ni = k_i + direct[0]
        k_nj = k_j + direct[1]

        # 킹의 새로운 좌표가 체스판 안에 있는 경우(cmd 시행 아직 가능)
        if 0 < k_ni <= 8 and 0 < k_nj <= 8:
            if k_ni != s_i or k_nj != s_j: # 이동할 위치 != 현재 돌 위치
                lst[k_i][k_j] = 0
                k_i, k_j = k_ni, k_nj
                lst[k_i][k_j] = 1
            else:                          # 이동할 위치 == 현재 돌 위치
                s_ni = s_i + direct[0]
                s_nj = s_j + direct[1]
                # 돌의 새로운 좌표가 체스판 안에 있는 경우
                if 0 < s_ni <= 8 and 0 < s_nj <= 8:
                    lst[k_i][k_j] = 0
                    k_i, k_j = k_ni, k_nj
                    lst[k_i][k_j] = 1
                    s_i, s_j = s_ni, s_nj
                    lst[s_i][s_j] = 2

    k_j = chr(k_j + 64)
    k_i = str(k_i)
    s_j = chr(s_j + 64)
    s_i = str(s_i)

    k_result = k_j + k_i
    s_result = s_j + s_i
    print(k_result)
    print(s_result)


