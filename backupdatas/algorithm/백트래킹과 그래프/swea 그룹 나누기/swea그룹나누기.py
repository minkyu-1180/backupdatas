# swea 그룹 나누기
import sys
sys.stdin = open("swea그룹나누기input.txt")

# 본인의 부모 노드 찾는 함수
# find_set: x를 포함하는 집합을 찾는 연산
def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])
# x와 y를 포함하는 두 집합을 통합하는 연산
def union(x,y):
    p[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    p = [i for i in range(N+1)]

    for i in range(0, 2*M, 2):
        parent = arr[i]
        child = arr[i+1]
        union(parent, child)

    result = set()
    for i in range(1, N+1):
        result.add(find_set(i))

    print(f'#{tc} {len(result)}')