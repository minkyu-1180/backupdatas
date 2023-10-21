# 백준 2869. 달팽이는 올라가고 싶다
import sys
sys.stdin = open("bj2869input.txt")

# 원래 T는 없음
T = int(input())
for tc in range(T):
    # A : 낮에 A미터 올라갈 수 있어요
    # B : 밤에 자는 동안 B미터 미끄러져요
    # V : 나무 막대는 V미터이다
    # 1 <= B < A <= V <= 1000000000)
    A, B, V = map(int, input().split())
    day = (V-A)//(A-B)
    last = (V-A)%(A-B)
    if last:
        print(day+2)
    else:
        print(day+1)

