# 백준 2670. 연속부분최대곱
import sys
sys.stdin = open("bj2670input.txt")
'''
[1.1, 0.7, 1.3, 0.9, 1.4, 0.8, 0.7, 1.4]
구간 곱?
갱신
'''
N = int(input())
arr = []
for i in range(N):
    num = float(input())
    arr.append(num)
# print(arr)
result = []
result.append(arr[0])
for i in range(1, N):
    result.append(max(arr[i], result[i-1] * arr[i]))
# print(round(max(result), 3))
print('%.3f' % max(result))