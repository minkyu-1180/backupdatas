# sw academy - 4836. 색칠하기
import sys
sys.stdin = open("../input.txt")
from pprint import pprint as pp
T = int(input())
for test_case in range(1, T+1):
    # 첫 줄에 칠할 영역의 개수
    N = int(input())
    # all arr : 칠하는 영역의 개수만큼의 행을 가진 각 칠하는실행의 영역 / 색상 정보
    all_arr = [list(map(int, input().split())) for _ in range(N)]
    # all_arr[i][0] : x1 / all_arr[i][1] : x2
    # all_arr[i][2] : y1 / all_arr[i][3] : y2
    # all_arr[i][4]: color

    # red / blue 구분
    blue_arr = []
    red_arr = []

    for ele in all_arr:
        # color = red
        if ele[4] == 1:
            red_arr.append(ele)
        else:
            blue_arr.append(ele)

    # 결과값
    result = 0
    # 해당 index에 색칠된 색이 무엇인지 보여주는 2차원 배열(1 : red / 2 : blue / 3 : purple)
    result_arr = [[0] * 10 for _ in range(10)]
    for red in red_arr:
        x1 = red[0]
        x2 = red[2]
        y1 = red[1]
        y2 = red[3]
        for j in range(x1, x2 + 1):
            for i in range(y1, y2 + 1):
                # 칠해야 하는데 아직 안칠해진 경우 칠해줌(이미 빨간색이면 굳이)
                if result_arr[i][j] != 1:
                    result_arr[i][j] += 1

    for blue in blue_arr:
        x1 = blue[0]
        x2 = blue[2]
        y1 = blue[1]
        y2 = blue[3]
        for j in range(x1, x2 + 1):
            for i in range(y1, y2 + 1):
                # 이미 파란색이 칠해지지 않은 경우 칠해주거나 덧발라줌
                if result_arr[i][j] != 2:
                    result_arr[i][j] += 2
    # 결국 원하는 것은 보라색, 즉 3의 개수
    for i in range(10):
        for j in range(10):
            if result_arr[i][j] == 3:
                result += 1
    print(f'#{test_case} {result}')