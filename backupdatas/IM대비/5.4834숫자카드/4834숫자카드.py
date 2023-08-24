# IM 대비 5. 숫자카드
import sys
sys.stdin = open("숫자카드input.txt")
T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 숫자카드 개수 (5 <= N <= 100)
    # 여백없이 N개의 숫자 input
    arr = list(map(int, input()))

    result = [0] * 10 # result[i] : i가 쓰여있는 카드 개수
    for num in arr:
        result[num] += 1

    idx = 0 # 가장 많은 카드의 숫자(동률시 더 큰 번호)
    for i in range(1, 10):
        if result[idx] <= result[i]: # 동률시 더 큰 번호 선정
            idx = i
    print(f'#{test_case} {idx} {result[idx]}')
