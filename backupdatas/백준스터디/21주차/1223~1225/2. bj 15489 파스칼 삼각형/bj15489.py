# 백준 15489. 파스칼 삼각형
import sys
from pprint import pprint
sys.stdin = open("bj15489input.txt")


arr = [[0] * 30 for _ in range(30)]
for i in range(30):
    arr[i][i] = 1
    arr[i][0] = 1
for i in range(2, 30):
    for j in range(30):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
# for lst in arr:
#     print(lst)

'''
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
...

arr[2][1] = arr[1][0] + arr[1][1]
arr[
'''

# R, C, W -> R번째 줄, C번째 수를 위 꼭짓점으로 하는
# 한 변이 포함하는 수의 개수가 W인 정삼각형
R, C, W = map(int, input().split())
result = 0
c = 1
for i in range(R-1, R-1+W):
    for j in range(C-1, C-1+c):
        result += arr[i][j]
    c += 1
print(result)