# 백준 28278. 스택 2
import sys
sys.stdin = open("28278input.txt")

N = int(input())
stack = []
for _ in range(N):
    # input()으로 받을 때랑 input().split()으로 받을 때의 차이는?
    cmd = input().split()
    '''
    명령어의 종류
    1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
    2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
    3: 스택에 들어있는 정수의 개수를 출력한다.
    4: 스택이 비어있으면 1, 아니면 0을 출력한다.
    5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
    '''
    if cmd[0] == '1':
        stack.append(int(cmd[1]))
    elif cmd[0] == '2':
        # 스택에 원소가 있을 경우
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd[0] == '3':
        print(len(stack))
    elif cmd[0] == '4':
        if stack == []:
            print(1)
        else:
            print(0)
    elif cmd[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)
