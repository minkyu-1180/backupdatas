# 백준 26069. 붙임성 좋은 총ㅇ총이
import sys
sys.stdin = open("bj26069input.txt")

N = int(input())
my_set = set()
my_set.add('ChongChong')

for _ in range(N):
    name_1, name_2 = input().split()
    if name_1 in my_set and name_2 not in my_set:
        my_set.add(name_2)
    elif name_2 in my_set and name_1 not in my_set:
        my_set.add(name_1)
print(len(my_set))