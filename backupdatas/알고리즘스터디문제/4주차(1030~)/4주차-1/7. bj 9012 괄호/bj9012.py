# 백준 9012. 괄호
import sys
sys.stdin = open("bj9012input.txt")

# 원래 T는 없음
T = int(input())
for tc in range(T):
    N = int(input())
    for _ in range(N):
        string = input()
        result = 0
        K = len(string) // 2
        c = 0
        while c < K:
            string = string.replace('()', '')
            c += 1
            if len(string) <= 1:
                break
        if len(string) == 0:
            print('YES')
        else:
            print('NO')
