# IM 대비 14. Ladder2
import sys
sys.stdin = open("Ladder2input.txt")
for test_case in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    result = 0
    min_dist = 10000
    # 모든 출발점을 검사
    for j in range(100):
        if arr[0][j] == 1:
            c = 0
            x, y = j, 0 # j에 대한 반복 -> j값을 담아주는 변수 필요
            while y < 99:
                # 오른쪽 이동 가능
                if x < 99 and arr[y][x+1]:
                    while x < 99 and arr[y][x+1]:
                        x += 1
                        c += 1
                    else:
                        y += 1
                # 왼쪽 이동 가능
                elif x > 0 and arr[y][x-1]:
                    while x > 0 and arr[y][x-1]:
                        x -= 1
                        c += 1
                    else:
                        y += 1

                # 밑으로 이동(왼/오 다 막힘)
                elif arr[y+1][x] == 1:
                    y += 1
                    c += 1
            # i == 99 -> while문 탈출 후 최소 거리 갱신
            if min_dist > c:
                min_dist = c
                result = j


    print(f'#{tc} {result}')
    '''
        result = 0
        min_dist = 10000 # 최대 거리
        start = []
        for j in range(100):
            # 출발점의 x좌표
            if arr[0][j] == 1:
                c = 0 # 거리
                i = 0 # 시작 row idx
                while i < 99:
                    if 0 <= j+1 < 100 and arr[i][j+1] == 1:
                        while 0 <= j+1 < 100 and arr[i][j+1] == 1:
                            c += 1
                            j += 1
                    elif 0 <= j-1 < 100 and arr[i][j-1] == 1:
                        while 0 <= j-1 < 100 and arr[i][j-1] == 1:
                            c += 1
                            j -= 1

                    c += 1
                    i += 1

                    if i == 99 and min_dist > c:
                        min_dist = c
                        result = j


        print(f'#{test_case} {result} ')
    '''