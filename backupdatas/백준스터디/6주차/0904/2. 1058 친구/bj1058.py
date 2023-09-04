# 백준 1058. 친구
import sys
sys.stdin = open("bj1058input.txt")
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = [[0] * N for _ in range(N)]
    for c in range(N):
        for a in range(N):
            for b in range(N):
                if (a != b) and ((arr[a][b] == 'Y') or (arr[a][c] == 'Y' and arr[b][c] == 'Y')):
                    result[a][b] = 1
    max_c = 0
    for r in result:
        if max_c < sum(r):
            max_c = sum(r)
    print(max_c)





