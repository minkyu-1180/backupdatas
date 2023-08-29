# 장태수님 - 풍선 터뜨리기
import sys
from collections import deque

input = sys.stdin.readline

# 풍선의 개수
N = int(input())

# map type에 대해 enumerate 시행 -> 해당 요소들에 대해 idx, val을 tuple로 묶어줌
# que = deque([(0, 3), (1, 2), (2, 1), (3, -3), (4, -1)])
que = deque(enumerate(map(int, input().split())))
result = [0] * N

idx = 0
# 큐의 모든 풍선들이 빠질 때 까지 진행
while que:
    i, v = que.popleft() # 1번 풍선부터 진행
    result[idx] = i+1

    # 현재 큐 내의 i번 idx의 값 : popleft 진행 전 i+1번 idx
    # 풍선 안에 있는 숫자 : -N ~ -1, 1 ~ N

    # rotate는 직접 그림을 그려서 해보면 쉽게 이해 가능
    if v > 0: # 풍선 안의 숫자가 양수일 경우(원형 큐 형태 -> 현재 바라보는 인덱스 번호가 반시계 방향으로 돌아가게 조정)
        que.rotate(-(v-1)) # 반시계 방향으로 v-1만큼 회전(pop을 통해 큐의 길이가 줄어서)
    elif v < 0: # 풍선 안의 숫자가 음수일 경우(현재 바라보는 인덱스 번호가 시계 방향으로 돌아가게 조정)
        que.rotate(-v) # 시계 방향으로 abs(v)만큼 회전
    idx += 1
print(result)