# 백준 1527. 금민수의 개수
import sys
sys.stdin = open("bj1527input.txt")
from collections import deque
# 원래 T는 없음
T = int(input())
for tc in range(T):
    # 1 <= A <= B <= 1000000000
    A, B = map(int, input().split())
    que = deque()
    que.append('4')
    que.append('7')
    result = 0
    while que:
        now = que.popleft()

        if int(now) <= B:
            que.append(now + '4')
            que.append(now + '7')
            if A <= int(now):
                result += 1
    print(result)
