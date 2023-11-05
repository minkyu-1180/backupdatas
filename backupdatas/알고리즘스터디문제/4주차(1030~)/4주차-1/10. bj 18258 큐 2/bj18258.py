# 백준 18258. 큐 2
import sys
from collections import deque
sys.stdin = open("bj18258input.txt")

que = deque()
# N : 명령의 수 (1 <= N <= 2000000)
N = int(input())
for _ in range(N):
    cmd = list(input().split())
    if cmd[0] == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)

    elif cmd[0] == 'size':
        print(len(que))
    elif cmd[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)

    else:
        que.append(int(cmd[1]))
