# 백준 10773. 제로
import sys
sys.stdin = open("bj10773input.txt")


# 원래 T는 없음
T = int(input())
for tc in range(T):
    # K : 주어지는 정수 개수(1 <= K <= 100000)
    K = int(input())
    arr = []
    for _ in range(K):
        num = int(input())
        # 0을 외치는 경우, 가장 최근 수 지우기
        if num == 0:
            arr.pop()
        else:
            arr.append(num)
    print(sum(arr))
