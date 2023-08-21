# sw academy 중위순회
import sys
sys.stdin = open("중위순회input.txt")

for test_case in range(1, 11):
    N = int(input()) # 1 <= N <= 100

    tree = [0] * (N+1)
    arr = [list(input().split()) for _ in range(N)]
    print(arr)