# 행렬 탐색 연습
# 0으로 초기화 된 N * M의 2차원 배열 생성

from pprint import pprint as pp

m = 5
n = 6
arr = []
for i in range(n):
    row = [0] * m
    arr.append(row)
pp(arr)

# 벽을 세운다 : 주어진 2차원 리스트의 범위를 벗어나지 않도록 제한하는 행위
# 1. 벽의 제한을 두는데, 벽을 넘어가는 경우 아무것도 하지 않는다
# 2. 벽을 넘어가지 않는 경우에만 수행한다

# map을 넘어가는 경우 아무것도 하지 않기
'''
if isSafeArea:
    continue
'''

# 벽을 넘어가지 않는 경우에 수행
'''
if nx <= 0 < N and 
'''