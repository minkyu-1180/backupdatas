# 백준 24723. 녹색거탑
import sys
sys.stdin = open("bj24723input.txt")

# 원래 T는 없음
T = int(input())
for tc in range(T):
    # 녹색거탑의 높이(1 <= N <= 5)
    N = int(input())
    print(2 ** N)
