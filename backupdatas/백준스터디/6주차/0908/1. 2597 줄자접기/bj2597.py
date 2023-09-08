# 백준 2597. 줄자 접기
import sys
sys.stdin = open("bj2597input.txt")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(3)]


ruler_len = N
while True:
    color = arr.pop(0)
    color_1, color_2 = color[0], color[1]
    if color_1 != color_2:
        middle = (color_1 + color_2) / 2
        # 줄자 길이 갱신
        ruler_len = max((ruler_len-middle), middle)
        # 나머지 색 위치 갱신
        if arr:
            for i in range(len(arr)):
                c_1, c_2 = arr[i][0], arr[i][1]
                c_1 = abs(middle-c_1)
                c_2 = abs(middle-c_2)
                arr[i] = [c_1, c_2]
        else:
            break
print(ruler_len)

