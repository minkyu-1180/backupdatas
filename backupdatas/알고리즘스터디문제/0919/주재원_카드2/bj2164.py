# 백준 2164. 카드
from collections import deque
import sys
sys.stdin = open('bj2164input.txt')
N = int(input())

que = deque(range(1, N+1))
while len(que) > 1:
    que.popleft()
    que.append(que.popleft())

print(que[0])