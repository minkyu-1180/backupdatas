# Magnetic
import sys
sys.stdin = open("Magneticinput.txt")

for test_case in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    result = 0
    for j in range(100):
        stack = []
        for i in range(100):
            if arr[i][j] == 1:
                if not stack:
                    stack.append(arr[i][j])
            elif arr[i][j] == 2:
                if stack:
                    stack.pop()
                    result += 1
    print(f'#{test_case} {result}')