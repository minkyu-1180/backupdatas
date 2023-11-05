# 백준 28278. 스택 2
import sys
sys.stdin = open("bj28278input.txt")

# N : 명령의 수(1<=N<=100000)
N = int(input())
stack = []
for _ in range(N):
    # 명령어의 종류
    cmd = input().split()
    # push
    if cmd[0] == '1':
        stack.append(int(cmd[1]))
    # pop
    elif cmd[0] == '2':
        # 스택에 원소가 있을 경우
        if stack:
            print(stack.pop())
        else:
            print(-1)
    # 스택 원소 개수 출력
    elif cmd[0] == '3':
        print(len(stack))
    # isEmpty
    elif cmd[0] == '4':
        if stack == []:
            print(1)
        else:
            print(0)
    # stack[top]
    elif cmd[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)