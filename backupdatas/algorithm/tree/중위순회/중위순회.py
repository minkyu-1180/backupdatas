# sw academy 중위순회
import sys
sys.stdin = open("중위순회input.txt")

# 중위순회 함수
def inorder(idx, N): # 방문중인 인덱스 / 노드번호 최대값
    if idx <= N:                    # 해당 인덱스가 트리 내의 인덱스인경우
        inorder(idx * 2, N)            # 왼쪽 자식 이동
        print(tree[idx], end = '')  # 중위순회에서 할 일
        inorder(idx * 2 + 1, N)        # 오른쪽 자식 이동

for test_case in range(1, 11):
    N = int(input()) # 1 <= N <= 100

    tree = [0] * (N+1)
    # 트리에 노드정보 입력
    for _ in range(N):
        node_info = list(input().split())
        idx = int(node_info[0])         # 해당 노드정보의 트리 인덱스
        node = node_info[1]             # 해당 노드값
        tree[idx] = node                # 적절한 인덱스에 노드값 할당
    # print(tree)
    print(f'#{test_case}', end = ' ')
    inorder(1, N)
    # 혹시 이런 문제에서 end때문에 일렬로 나오는 경우를 방지하기 위해
    # 만약 테스트케이스가 한 개이면 두개로 복사해서 일렬로 출력되는지 확인해보기
    print()
