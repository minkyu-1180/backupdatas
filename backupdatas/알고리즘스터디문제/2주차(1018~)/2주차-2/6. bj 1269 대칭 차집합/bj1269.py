# 백준 1269. 대칭 차집합
import sys
sys.stdin = open("bj1269input.txt")


# A : 공집합이 아닌 집합 A의 원소 개수
# B : 공집합이 아닌 집합 B의 원소 개수
A, B = map(int, input().split())
set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))
print(len(set_A - set_B) + len(set_B - set_A))