# 백준 2164. 카드 2
import sys
from collections import deque
sys.stdin = open("bj2164input.txt")


N = int(input())

que = deque(range(1, N+1))
while len(que) > 1:
    que.popleft()
    que.append(que.popleft())

print(que[0])