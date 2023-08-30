# 풍선 터뜨리기
import sys
from collections import deque

sys.stdin = open("ballooninput.txt")

N = int(input()) # 풍선 개수(1<=N<=1000)


# 원형큐 생성
arr = list(map(int, input().split()))
que = deque([])
for i, v in enumerate(arr):
    que.append([i, v])

# 터진 풍선의 순서를 담을 리스트
result = []

while que:
    # 현재 보는 idx의 풍선 터뜨리기
    i, v = que.popleft()
    # print(que)
    result.append(i+1) # 터뜨린 풍선 번호(= idx + 1)을 결과에 추가

    # 현재 i가 바라보고 있는 값 : 기존 i+1에 들어있던 값
    if v > 0: # 양수 -> 반시계로 rotate(rotate에 들어가는 인수가 음수가 되게끔)
        que.rotate(-(v-1))
    else: # 음수 -> 시계로 rotate(rotate에 들어가는 인수가 양수가 되게끔)
        que.rotate(-v)
    # print(que)

print(*result)

