# 초심자의 회문 검사
import sys
sys.stdin = open("reversetestinput.txt")

T = int(input())
for test_case in range(1, T+1):
    arr = list(input())
    n = len(arr)
    result = [0] * n
    for i in range(n):
        result[i] = arr[n-i-1]
    if result == arr:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')