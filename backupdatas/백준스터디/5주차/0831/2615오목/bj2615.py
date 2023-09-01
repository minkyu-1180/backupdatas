# 백준 2615. 오목
import sys
sys.stdin = open("2615input.txt")

arr = [list(map(int, input().split())) for _ in range(19)]

'''
누구의 알이 더 많은가? 확인해야 하나? -> 동시에 이기는 경우 x
어디까지 봐야 하나?
여섯 알 이상이 연속적으로 놓인 경우는 이긴게 아님

'''
# 위에서 아래로
for i in range(19):
    for j in range(19):
        if arr[i][j] != 0:
            c = arr[i][j]



