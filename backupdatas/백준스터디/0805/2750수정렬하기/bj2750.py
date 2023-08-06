# 2750. 수 정렬하기
import sys
sys.stdin = open("2750input.txt")
# 주어지는 수의 개수
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

for i in range(N-1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

for i in range(N):
    print(arr[i])
