import sys
sys.stdin = open("10828input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    '''
    push X: 정수 X를 스택에 넣는 연산이다.
    pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    size: 스택에 들어있는 정수의 개수를 출력한다.
    empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
    top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    '''
    stack = []
    for _ in range(N):
        cmd = input().split()
        # push인 경우
        if cmd[0] == 'push':
            stack.append(int(cmd[1]))

        # pop인 경우
        elif 'pop' in cmd:
            if stack:
                popitem = stack.pop()
                print(popitem)
            else:
                print(-1)

        # size인 경우
        elif 'size' in cmd:
            print(len(stack))

        # empty인 경우
        elif 'empty' in cmd:
            if stack:
                print(0)
            else:
                print(1)
        # top인 경우
        elif 'top' in cmd:
            if stack:
                print(stack[-1])
            else:
                print(-1)