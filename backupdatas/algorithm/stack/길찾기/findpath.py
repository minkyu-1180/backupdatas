# 길찾기
import sys
sys.stdin = open("findpathinput.txt")


# DFS 함수
def DFS(adj_1, adj_2, start, end):
    stack = []
    visited = [0] * 100
    visited[start] = 1

    while True:
        for next in range(100):
            if (adj_1[start] == next or adj_2[start] == next) and visited[next] == 0:
                stack.append(start)
                start = next
                visited[start] = 1
                break
        else:
            if stack:
                start = stack.pop()
            else:
                break
    return visited[end]


for test_case in range(1, 11):
    tc, N = map(int, input().split())
    arr = list(map(int, input().split()))

    # 각 arr의 index는 곧 node의 번호
    # 각 arr의 index에 할당된 값은 곧 node와 인접한 노드
    arr1 = [0] * 100
    arr2 = [0] * 100

    for i in range(0, len(arr), 2):
        if arr1[arr[i]] == 0:
            arr1[arr[i]] = arr[i+1]
        else:
            arr2[arr[i]] = arr[i+1]
    print(f'#{test_case} {DFS(arr1, arr2, 0, 99)}')
