# 2669. 직사각형 네 개의 합집합의 면적 구하기
import sys
sys.stdin = open("2669input.txt")

# (0, 0)부터 (100, 100)까지 1사분면 좌표 표현
result = [[0] * 101 for _ in range(101)]
# 총 4개의 (x1 ~ x2), (y1 ~ y2) 정보 제공
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    # y : y1 ~ y2-1
    for y in range(y1, y2):
        # x : x1 ~ x2-1
        for x in range(x1, x2):
            # result[y][x] : (x, y)좌표에 표시된 값
            if result[y][x] == 0: # 만약 표시되지 않은 경우(그려야하는데 아직 안그려진 경우)
                result[y][x] = 1
c = 0
for i in range(101):
    for j in range(101):
        if result[i][j] == 1:
            c += 1
print(c)

