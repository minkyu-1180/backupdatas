# 백준 10845. 큐
import sys
sys.stdin = open("bj10845input.txt")

import sys
input = sys.stdin.readline

N = int(input()) # 1 <= N <= 10000
queue = []

def enqueue(x):
    queue.append(x)
    return

def dequeue():
    if queue:
        return queue.pop(0)

    return -1

def size():
    return len(queue)

def isempty():
    if queue:
        return 0
    return 1

def front():
    if queue:
        return queue[0]
    return -1

def rear():
    if queue:
        return queue[-1]
    return -1


for _ in range(N):
    cmd = input().split()
    '''
    명령어 종류
    push X: 정수 X를 큐에 넣는 연산이다.
    pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    size: 큐에 들어있는 정수의 개수를 출력한다.
    empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
    front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    '''
    if cmd[0] == 'push':
        enqueue(cmd[1])
    elif cmd[0] == 'pop':
        print(dequeue())
    elif cmd[0] == 'size':
        print(size())
    elif cmd[0] == 'empty':
        print(isempty())
    elif cmd[0] == 'front':
        print(front())
    elif cmd[0] == 'back':
        print(rear())