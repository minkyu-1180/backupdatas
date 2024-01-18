# 백준 17615. 볼 모으기
import sys
sys.stdin = open("bj17615input.txt")

def check_l(color):
    global result

    left = [0, 0]
    # 앞에서부터
    for i in range(N):
        # 같은색 -> 개수 추가
        if arr[i] == color:
            left[0] += 1

        # 다른 색인데 쌓여있는 경우 -> count 추가
        elif left[0] > 0:
            left[1] += left[0]
            left[0] = 0

    result = min(result, left[1])
    return


def check_r(color):
    global result

    right = [0, 0]
    # 뒤에서 부터
    for i in range(N-1, -1, -1):
        # 같은 색 -> 개수 추가
        if arr[i] == color:
            right[0] += 1
        # 다른색인데 이미 쌓여있는 경우 -> 뛰어넘기
        elif right[0] > 0:
            right[1] += right[0]
            right[0] = 0

    result = min(result, right[1])
    return


# arr 원래 T는 없음
T = int(input())
for tc in range(T):
    # N : 볼의 총 개수(1 <= N <= 500000)
    N = int(input())
    # 초기 공 상태
    arr = list(input())
    result = int(1e9)

    check_l("R")
    check_r("R")
    check_l("B")
    check_r("B")

    print(result)