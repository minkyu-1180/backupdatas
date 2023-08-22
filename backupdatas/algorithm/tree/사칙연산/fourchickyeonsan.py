# sw academy 사칙연산
import sys
sys.stdin = open("사칙연산input.txt")

for test_case in range(1, 11):
    N = int(input())
    child_info = [[] for _ in range(N+1)]

    tree = [0] * (N+1)
    for i in range(1, N+1):
        arr = list(input().split())
        # arr의 길이는 무조건 2 아니면 4(자식노드쌍 존재)
        if len(arr) == 4:
            child_info[i].append(int(arr[2]))
            child_info[i].append(int(arr[3]))
            tree[i] = arr[1]
        else:
            tree[i] = int(arr[1])

    # print(tree)
    # print(child_info)
    for i in range(N, 0, -1):
        # 자식노드가 있는 경우만 연산 시행
        if child_info[i]:
            num1_idx = child_info[i][0] # 왼쪽 자식 노드
            num2_idx = child_info[i][1] # 오른쪽 자식 노드
            num1 = tree[num1_idx]
            num2 = tree[num2_idx]
            # 연산자가 들어있는 tree의
            if tree[i] == '+':
                tree[i] = num1 + num2
            elif tree[i] == '-':
                tree[i] = num1 - num2
            elif tree[i] == '*':
                tree[i] = num1 * num2
            elif tree[i] == '/':
                tree[i] = num1 // num2
    print(f'#{test_case} {tree[1]}')