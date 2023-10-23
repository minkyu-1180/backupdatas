# 백준 4153. 직각삼각형
import sys
sys.stdin = open("bj4153input.txt")

# 세 변의 길이
# arr = [0, 0, 0]일 경우, 종료
arr = list(map(int, input().split()))

while True:
    if arr == [0, 0, 0]:
        break
    # 가장 큰 변 찾기 위해 오름차순 정렬
    arr.sort()
    x, y, z = arr
    if x**2 + y**2 == z**2:
        print('right')
    else:
        print('wrong')

    arr = list(map(int, input().split()))