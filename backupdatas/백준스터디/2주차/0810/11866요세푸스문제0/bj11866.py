# 요세푸스 문제 O
import sys
sys.stdin = open("11866input.txt")

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(range(1, N+1))
    stack = []
    i = 0
    while arr:
        i = (i + K - 1) % len(arr)
        stack.append(arr.pop(i))

    print('<', end = '')
    for i in range(len(stack)-1):
        print(stack[i], end = ', ')
    print(stack[-1], end = '')
    print('>')

