# 10989. 수 정렬하기 3
# 메모리 초과 방지(input = sys.stdin.readline)
import sys
sys.stdin = open("10989input.txt")

N = int(input())

arr = [0] * 10001
# arr의 i번 index에는 i의 개수가 할당
for _ in range(N):
    arr[int(input())] += 1

for i in range(10001):
    # 입력 받은 N개의 숫자 중 i가 존재할 경우
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)




