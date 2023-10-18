# 백준 25305. 커트라인
import sys
sys.stdin = open("bj25305input.txt")

# N : 응시자의 수(1<=N<=1000)
# K : 상을 받는 사람의 수(1<=K<=N)
N, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort() # 오름차순 정렬
# 뒤에서 K번째로 오는 원소 출력
print(arr[-K])