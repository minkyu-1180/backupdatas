# 백준 1715. 카드 정렬하기
import sys
sys.stdin = open("bj1715input.txt")
import heapq

N = int(input())
pq = []
for _ in range(N):
    # 왜 append로 하면 안될까??
    heapq.heappush(pq, int(input()))
result = 0

while len(pq) > 1:
    num1 = heapq.heappop(pq)
    num2 = heapq.heappop(pq)
    result += (num1+ num2)
    heapq.heappush(pq, num1+num2)

print(result)


