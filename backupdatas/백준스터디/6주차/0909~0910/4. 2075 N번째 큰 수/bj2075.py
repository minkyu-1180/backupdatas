# 백준 2075. N번째 큰 수
import sys
sys.stdin = open("bj2075input.txt")
import heapq

N = int(input())
heap = []

for _ in range(N):
    arr = list(map(int, input().split()))
    for num in arr:
        # 아직 N개 안채움
        if len(heap) < N:
            heapq.heappush(heap, num)
        # N개 채움 -> 교환 결정
        else:
            # 최소힙 root 원소가 더 작을 경우 -> 교환
            if heap[0] < num:
                heapq.heappop(heap)
                # 푸쉬만 해주면 알아서 순서에 맞게 배치됨
                heapq.heappush(heap, num)
print(heap[0])

'''
메모리 초과 남
count = 1
max_v = 0
# info[j] : jth col에서 보고 있는 row idx번호
info = [N-1] * N

lst = [arr[N-1][j] for j in range(N)]
while count <= N:
    max_v = max(lst)
    max_v_j = lst.index(max_v) # 몇 번 col에 가장 큰 값이 있나요?
    info[max_v_j] -= 1
    lst[max_v_j] = arr[info[max_v_j]][max_v_j]
    count += 1

print(max_v)
'''
