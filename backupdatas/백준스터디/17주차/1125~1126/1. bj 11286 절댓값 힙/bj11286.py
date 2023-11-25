# 백준 11286. 절댓값 힙
import sys
import heapq
sys.stdin = open("bj11286input.txt")

# N : 연산의 개수(1 <= N <= 100000)
N = int(input())

pq = []
for _ in range(N):
    # x : 연산에 대한 정보를 나타내는 정수
    x = int(input())

    # x != 0 -> heapq.heappush
    if x:
        heapq.heappush(pq, (abs(x), x))
    # x == 0 -> heapq.heappop
    else:
        # pq에 값 존재 -> 절댓값이 가장 작은 값 출력
        if pq:
            ele = heapq.heappop(pq)
            print(ele[1])
        # pq에 값 X -> 0 출력
        else:
            print(0)