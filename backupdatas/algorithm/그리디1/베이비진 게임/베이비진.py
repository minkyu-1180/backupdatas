# sw academy 베이비진
import sys
sys.stdin = open("베이비진input.txt")

def runs(i, lst):
    # 1. i-2, i-1, i
    if i-2 >= 0:
        if lst[i-2] > 0 and lst[i-1] > 0 and lst[i] > 0:
            return True
    if i - 1 >= 0 and i + 1 < 10:
        if lst[i-1] > 0 and lst[i] > 0 and lst[i+1] > 0:
            return True
    if i+2 < 10:
        if lst[i] > 0 and lst[i+1] > 0 and lst[i+2] > 0:
            return True
    return False

def tri(i, lst):
    if lst[i] >= 3:
        return True
    return False

T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input().split()))

    result1 = [0] * 10
    result2 = [0] * 10
    result = 0
    for i in range(12):
        num = arr[i]
        if i%2 == 0:
            result1[num] += 1
            if runs(num, result1) or tri(num, result1):
                result = 1
                break
        else:
            result2[num] += 1
            if runs(num, result2) or tri(num, result2):
                result = 2
                break

    print(f'#{test_case} {result}')