# 백준 2785. 체인
import sys
sys.stdin = open("bj2785input.txt")
T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    if N == 2:
        result = 1
    else:
        result = 0
        arr.sort()
        while len(arr) > 1:
            c = arr.pop(0)
            while c > 0:
                if len(arr) == 1:
                    result += 1
                    break
                c -= 1
                num1 = arr.pop()
                num2 = arr.pop()
                arr.append(num1+num2+1)
                result += 1
    print(result)


