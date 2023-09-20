# 백준 14890. 경사로
import sys
sys.stdin = open("bj14890input.txt")

def make_slope(lst):
    for i in range(1, N):
        # 인접 높이가 2이상 차이 날 때
        if abs(lst[i] - lst[i-1]) > 1:
            return False
        # 앞에꺼보다 1만큼 더 낮을 때
        if lst[i] - lst[i-1] == -1:
            # i ~ i+L-1까지 높이 통일, 아직 경사로 건설 X이어야 함
            for k in range(L):
                if i+k >= N or lst[i+k] != lst[i] or visited[i+k]:
                    return False
                visited[i+k] = 1
        # 앞에꺼보다 1만큼 높을 때
        if lst[i] - lst[i-1] == 1:
            # i-L ~ i-1까지 높이 통일, 아직 경사로 건설 X여야 함
            for k in range(1, L+1):
                if i-k < 0 or lst[i-k] != lst[i-1] or visited[i-k]:
                    return False
                visited[i-k] = 1
    return True

T = int(input())
for tc in range(T):
    N, L = map(int, input().split())
    arr1 = [list(map(int, input().split())) for _ in range(N)]
    arr2 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr2[i][j] = arr1[j][i]

    result = 0
    for i in range(N):
        visited = [0] * N
        lst1 = arr1[i]
        if make_slope(lst1):
            result += 1
        visited = [0] * N
        lst2 = arr2[i]
        if make_slope(lst2):
            result += 1
    print(result)