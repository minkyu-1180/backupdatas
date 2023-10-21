# 백준 10815. 숫자 카드
import sys
sys.stdin = open("bj10815input.txt")

# N : 상근이가 가지고 있는 숫자 카드 개수(1 <= N <= 500000)
N = int(input())
# 숫자 카드에 적혀있는 정수
arr_N = list(map(int, input().split()))
# 1 <= M <= 500000
M = int(input())
# 상근이가 가지고 있는 숫자인지 아닌지를 구해야 할 M개의 정수
arr_M = list(map(int, input().split()))

# 바이너리 서치 사용
arr_N.sort()
# 결과를 담을 리스트
result = [0] * M
for i in range(M):
    num_M = arr_M[i]
    if num_M > arr_N[N-1] or num_M < arr_N[0]:
        continue
    else:
        start = 0
        end = N-1
        while start <= end:
            middle = (start+end)//2
            num_N = arr_N[middle]
            if num_N == num_M:
                result[i] = 1
                break

            if num_N > num_M:
                end = middle-1
            elif num_N < num_M:
                start = middle+1
print(*result)
