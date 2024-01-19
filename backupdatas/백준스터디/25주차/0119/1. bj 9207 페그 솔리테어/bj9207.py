# 백준 9207. 페그 솔리테어
import sys
sys.stdin = open("bj9207input.txt")

def backtracking(arr, cnt2):
    global result1, result2

    cnt1 = 0
    # 현재 arr 상태에서 cnt 줄이기 가능?
    flag = False
    for i in range(5):
        for j in range(9):
            if arr[i][j] == "o":
                cnt1 += 1
                for di, dj in dir:
                    ni = i + di
                    nj = j + dj
                    # 뛰어넘기 가능한 상황
                    if 0 <= ni+di < 5 and 0 <= nj+dj < 9 and arr[ni][nj] == "o" and arr[ni+di][nj+dj] == ".":
                        arr[i][j] = "."
                        arr[ni][nj] = "."
                        arr[ni+di][nj+dj] = "o"
                        flag = True
                        backtracking(arr, cnt2+1)
                        arr[i][j] = "o"
                        arr[ni][nj] = "o"
                        arr[ni+di][nj+dj] = "."
    if not flag:
        if result1 > cnt1:
            result1 = cnt1
            result2 = cnt2
        elif result1 == cnt1:
            if result2 < cnt2:
                result2 = cnt2
        return

T = int(input())
for tc in range(T):
    arr = []

    pins = []
    for i in range(5):
        lst = list(input())
        for j in range(9):
            if lst[j] == "o":
                pins.append((i, j))
        arr.append(lst)
    if tc < T-1:
        space = input()
    # print(pins)
    '''
    . : 빈칸
    o : 핀이 꽂혀있는 칸
    # : 구멍이 없는 칸
    
    핀 : 수평, 수직 방향으로 인접한 핀을 넘어서 그 핀의 다음 칸으로 이동 가능
    - 인접한 핀의 다음 칸은 피어있어야 함
    - 해당 인접한 핀은 제거됨
    - 초기 핀의 개수는 최대 8개
    '''
    # print(arr)
    # 핀의 최소 개수
    result1 = int(1e9)

    # 최소 이동 횟수
    result2 = int(1e9)
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    backtracking(arr, 0)
    print(result1, result2)
