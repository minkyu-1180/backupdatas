# 백준 2295. 세 수의 합
import sys
from itertools import combinations_with_replacement as cwr
sys.stdin = open("bj2295input.txt")


N = int(input())
arr = []
max_val = 0
two_sum = set()
for _ in range(N):
    arr.append(int(input()))
arr.sort()

for i in range(N):
    for j in range(N):
        two_sum.add(arr[i] + arr[j])

def max_result():
    for i in range(N-1, 0, -1):
        num = arr[i]
        for j in range(i):
            if num-arr[j] in two_sum:
                return num

print(max_result())


# arr.sort()
# idx = N-1
# result = 0
# while idx >= 1:
#     flag = False
#     result = arr[idx]
#     combis = cwr(arr[:idx], 3)
#     for combi in combis:
#         if result == sum(combi):
#             flag = True
#             break
#     if flag:
#         break
#     idx -= 1
# print(result)
