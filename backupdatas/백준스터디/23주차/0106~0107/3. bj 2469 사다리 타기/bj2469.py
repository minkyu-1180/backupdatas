# 백준 2469. 사다리 타기
import sys
sys.stdin = open("bj2469input.txt")

def change(up, down):
    # 찾아야 할 곳 위쪽 쭉 내려오기
    for i in range(len(up)):
        lst = up[i]
        for j in range(K-1):
            if lst[j] == '-':
                start_list[j], start_list[j+1] = start_list[j+1], start_list[j]
    # 찾아야 할 곳 아래쪽 쭉 올라가기
    for i in range(len(down)-1, -1, -1):
        lst = down[i]
        for j in range(K-1):
            if lst[j] == '-':
                end_list[j], end_list[j+1] = end_list[j+1], end_list[j]
    return



# 원래 T는 없음
T = int(input())
for tc in range(T):
    # K : 참가한 사람의 수(3 <= K <= 26)
    # N : 가로 막대가 놓일 전체 가로 줄의 수(3 <= N <= 1000)
    K = int(input())
    N = int(input())
    # 최종 순서
    end_list = list(input())

    # A ~ ?까지 K개의 연속된 대문자 영어
    start_list = list(chr(i) for i in range(65, 65+K))
    # print(start_list)
    # print(end_list)

    # arr[i][j] == * -> 가로 막대 X
    # arr[i][j] == - -> 가로 막대 O
    # arr[i][j] == ? -> 맞춰야하는 줄
    arr = [list(input()) for _ in range(N)]

    # up : [?, ?, .... , ?] 전까지 있던 모양
    up = []
    # down : [?, ?, ... , ?] 후의 모양양
    down = []
    flag = False
    for i in range(N):
        lst = arr[i]
        if lst == ['?'] * (K-1):
            flag = True
        elif flag:
            down.append(lst)
        else:
            up.append(lst)
    # print(start_list)
    # print(end_list)
    change(up, down)
    # print(start_list)
    # print(end_list)
    # print()

    # 우리가 찾으려는 부분 - 현재 start_list와 end_list 사이에 껴 있음
    result = ['*'] * (K-1)

    for i in range(K-1):
        # 서로 바꿔줘야 하는 상태 -> 바꿔주기
        if start_list[i] == end_list[i+1] and start_list[i+1] == end_list[i]:
            start_list[i], start_list[i+1] = start_list[i+1], start_list[i]
            result[i] = '-'
    # 바꿨을 때 같으면 출력
    if start_list == end_list:
        print("".join(result))
    # 안되는 경우면 X로 ㅛ시
    else:
        print("x" * (K-1))