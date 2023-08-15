# 백준 1406. 에디터
import sys
sys.stdin = open('1406input.txt')
input = sys.stdin.readline

T = int(input())

for test_case in range(1, T+1):
    arr = list(input().rstrip())
    stack = []

    # top의 위치 기준 왼쪽 : arr / 오른쪽 : stack
    N = int(input())
    for _ in range(N):
        cmd = list(input().split())

        # 왼쪽으로 커서 이동
        if cmd[0] == 'L':
            # 현재 커서 위치가 0이 아닐 경우
            if arr: # 비어있을 경우 커서 위치가 0
                stack.append(arr.pop())
                # print(arr, stack)
        # 오른쪽으로 커서 이동
        elif cmd[0] == 'D':
            # 현재 커서 위치가 len(arr)이 아닐 경우
            if stack: # 비어있을 경우 커서 위치가 top
                arr.append(stack.pop())
                # print(arr, stack)
        # top 값 삭제
        elif cmd[0] == 'B':
            if arr:
                arr.pop()
                # print(arr, stack)
        # 새로운 원소 top 위치에 추가
        if cmd[0] == 'P':
            arr.append(cmd[1])
            # print(arr, stack)

    arr.extend(reversed(stack))
    print(''.join(arr))

'''
    # print(arr)
    top = len(arr)

    N = int(input())
    # 커서 위치
    # 커서 초기화 : 가장 끝 문자열의 오른쪽
    # top이 있을 수 있는 위치 : 0, 1, 2, ,,, len(arr)
    # 0 ~ len(arr)-1 : idx번 왼쪽
    # len(arr) : 끝 인덱스 오른쪽
    for _ in range(N):
        
        L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
        D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
        B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
            삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
        P $	$라는 문자를 커서 왼쪽에 추가함
        
        # print(f'초기 top 위치 : {top}')
        cmd = list(input().split())

        if cmd[0] == 'L':
            if top > 0:
                top -= 1
                # print(f'L로 인해 변한 top의 위치 : {top}')
        elif cmd[0] == 'D':
            if top < len(arr):
                top += 1
                # print(f'D로 인해 변한 top의 위치 : {top}')
        elif cmd[0] == 'B':
            if top > 0:
                top -= 1
                # print(f'B로 인해 제거한 값 : {arr[top]}')
                # print(f'B로 인해 변한 top의 위치 : {top}')
                arr.remove(arr[top])

        else:
            # 삽입하는 방법
            arr.insert(top, cmd[1])
            top += 1

    print(''.join(arr))
'''