# 1979. 어디에 단어가 들어갈 수 있을까
# 다시 해보기
import sys
sys.stdin = open("wordinput.txt")
from pprint import pprint as pp

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    for i in range(N):
        c = 0
        for j in range(N):
            if arr[i][j] == 1:
                c += 1
            if j == N-1 or arr[i][j] == 0:
                if c == K:
                    result += 1
                c = 0
    print(result)
