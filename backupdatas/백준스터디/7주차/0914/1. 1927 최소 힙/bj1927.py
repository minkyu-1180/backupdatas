# 백준 1927. 최소 힙
import heapq
import sys
sys.stdin = open("bj1927input.txt")

N = int(input()) # 연산의 개수(1 <= N <= 100000)
heap = []

for _ in range(N):
    num = int(input()) # 연산에 대한 정보를 나타내는 정수
    if num > 0: # 자연수 -> 해당 값을 배열에 추가
        heapq.heappush(heap, num)

    else: # 0 -> 가장 작은 값 출력 후 제거
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)