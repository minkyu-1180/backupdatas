# 백준 1038. 감소하는 수
import sys
sys.stdin = open("bj1038input.txt")
T = int(input())
arr = [[0]*(10-i) for i in range(10)]

arr[0] = [1] * 10
for i in range(1, 10):
    for j in range(0, 10-i):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

# 누적합
soon_seo = [0] * 11
soon_seo[1] = sum(arr[0])
for i in range(2, 11):
    soon_seo[i] = soon_seo[i-1] + sum(arr[i-1])
print(soon_seo)
print(sum(soon_seo))



for tc in range(T):
    N = int(input())
    result = -1
    if N < 1023:
        for i in range(1, 11):
            if soon_seo[i-1] <= N < soon_seo[i]:
                now = soon_seo[i-1] - 1
                jalitsoo = i
                num = 0
                for x in range(0, i+1):
                    num += x * (10**x)
                c = 1
                while c < N-now:
                    if num




    print(result)

