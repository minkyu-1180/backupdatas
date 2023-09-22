# swea 2819. 격자판의 숫자 이어 붙이기
import sys
sys.stdin = open("swea2819input.txt")

def dfs(y, x, number):
    if len(number) == 7:
        return

T = int(input())
for tc in range(1, T+1):
    maps = [input().split() for _ in range(4)]

    result = set()

    dfs()