# 백준 2493. 탑
import sys
sys.stdin = open("bj2493input.txt")

N = int(input())
arr = [0] + list(map(int, input().split()))

stack = []
result = []
stack.append([1, arr[1]])
result.append(0)

for i in range(2, N+1):
    now = [i, arr[i]]
    while stack:
        if now[1] >= stack[-1][1]:
            stack.pop()
        else:
            result.append(stack[-1][0])
            break
    if stack == []:
        result.append(0)
    stack.append(now)

for i in range(len(result)):
    print(result[i], end = ' ')
print()