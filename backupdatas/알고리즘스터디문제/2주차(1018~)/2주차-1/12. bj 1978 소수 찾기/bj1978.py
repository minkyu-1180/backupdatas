# 백준 1978. 소수 찾기
import sys
sys.stdin = open("bj1978input.txt")

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

N = int(input())
arr = list(map(int, input().split()))
result = 0
for num in arr:
    if isPrime(num):
        result += 1
print(result)