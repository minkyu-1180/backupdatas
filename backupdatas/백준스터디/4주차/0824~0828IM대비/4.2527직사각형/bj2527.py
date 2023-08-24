# IM 대비 4. 백준 2527 직사각형
import sys
sys.stdin = open("2527직사각형input.txt")

for test_case in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # 겹치지 않는 경우
    if x1 > p2 or x2 > p1 or y1 > q2 or y2 > q1:
        print('d')
    # 겹치는 경우
    else:
        # x축이랑 y축이 동시에 겹칠 때 즉, 점일 때
        if (x1 == p2 or x2 == p1) and (y1 == q2 or y2 == q1):
            print('c')
        else:
            # x축만 겹칠 때
            if x1 == p2 or x2 == p1:
                print('b')
            # y축만 겹칠 때
            elif y1 == q2 or y2 == q1:
                print('b')
            # 겹치는 부분이 없을 때
            else:
                print('a')


