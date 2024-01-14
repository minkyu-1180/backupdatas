# 백준 15662. 톱니바퀴(2)
import sys
from collections import deque
sys.stdin = open("bj15662input.txt")

def change(n, d):
    # 움직이려는 톱니바퀴의 왼쪽 오른쪽 극 상태
    '''
            0
          7   1
        6       2
          5   3
            4


    '''

    now_l = arr[n][6]
    now_r = arr[n][2]

    # d 방향으로 rotate 진행
    arr[n].rotate(d)

    d_l = d
    d_r = d
    # 왼쪽 change
    for i in range(n-1, -1, -1):
        # i의 오른쪽과 i+1의 왼쪽(now_l) 값 비교
        if now_l == arr[i][2]:
            break
        # 한칸씩 땡겨서 앞으로 가며 비교
        now_l = arr[i][6]
        d_l *= -1
        arr[i].rotate(d_l)

    # 오른쪽 change
    for i in range(n+1, N):
        if now_r == arr[i][6]:
            break
        now_r = arr[i][2]
        d_r *= -1
        arr[i].rotate(d_r)

    return
# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N : 톱니바퀴의 수(1 <= T <= 1000)
    N = int(input())

    # N개의 톱니바퀴 초기 상태
    # 12시부터 시계방향 순서대로
    # N극은 0, S극은 1
    arr = []
    for _ in range(N):
        q = deque()
        state = input()
        for s in state:
            q.append(int(s))
        arr.append(q)
    # print(arr)


    # K : 회전 횟수(1 <= K <= 1000)
    K = int(input())
    for _ in range(K):
        # n번 톱니바퀴를 d의 방향으로 회전
        # d : 1 -> 시계 / -1 -> 반시계
        n, d = map(int, input().split())
        n -= 1
        change(n, d)

    result = 0
    for i in range(N):
        result += arr[i][0]
    print(result)
    # for i in range(N):
    #     print(arr[i])