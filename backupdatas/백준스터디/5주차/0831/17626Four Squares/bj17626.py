# 백준 17626. Four Squares
import sys
sys.stdin = open("17626input.txt")


N = int(input()) # 1 <= N <= 50000
result = 4
sqr = [i**2 for i in range(1, int(N**0.5)+1)]

# print(sqr)
if N in sqr:
    print(int(N**0.5))
    result = 1
else:
    for i in range(int(N**0.5), 0, -1):
        if (N-i**2) in sqr:
            print(i**2, N-i**2)
            result = 2
            break
        else:
            for j in range(int((N-i**2)**0.5), 0, -1):
                if N - i**2 - j**2 in sqr:
                    print(j**2, i**2, N-i**2-j**2)
                    result = 3
print(result)


N = int(input())
arr = [0] * (N+1)
for i in range(1, int(N**0.5)+1):
    arr[i**2] = 1

result = 4
for i in range(int(N**0.5), 0, -1):
    if arr[N] : # n이 제곱수일 경우
        result = 1
        break
    elif arr[N-i**2] : # 나머지가 제곱수일 경우
        result = 2
        break
    else:
        for j in range(int((N-i**2)**0.5), 0, -1):
            if arr[(N-i**2)-j**2]: # 제곱수를 한번 더 뺀 나머지가 제곱수일 경우
                result = 3
print(result)