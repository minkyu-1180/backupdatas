# 백준 11651. 좌표 정렬하기 2
import sys
sys.stdin = open("bj11651input.txt")

# N : 점의 개수(1<=N<=100000)
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
# y 작은 순 -> y가 같으면 x가 작은 순
arr.sort(key=lambda x : (x[1], x[0]))

for x, y in arr:
    print(x, y)