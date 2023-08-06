# 23968. 알고리즘 수업 - 버블 정렬 1
import sys
sys.stdin = open("23968input.txt")

N, K = map(int, input().split())
arr = list(map(int, input().split()))

c = 0
ans = '-1'

# 버블 정렬
for i in range(N-1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            c += 1
            arr[j], arr[j+1] = arr[j+1], arr[j]

            if c == K:
                ans = f'{arr[j]} {arr[j+1]}'
print(ans)


