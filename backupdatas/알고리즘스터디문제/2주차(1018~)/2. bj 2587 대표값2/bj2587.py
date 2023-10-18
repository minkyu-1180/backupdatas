# 백준 2587. 대표값2
import sys
sys.stdin = open("bj2587input.txt")
# 5개의 입력값을 원소로 하는 배열
arr = []
for _ in range(5):
    arr.append(int(input()))
# 평균
print(sum(arr)//5)
# 중앙값
print(sorted(arr)[2])