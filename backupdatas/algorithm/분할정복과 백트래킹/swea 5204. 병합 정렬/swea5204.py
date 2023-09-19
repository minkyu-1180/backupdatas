# swea 5204. 병합 정렬
import sys
sys.stdin = open("swea5204input.txt")

def merge(left, right):
    global result_2

    l = r = 0
    result = []
    if left[-1] > right[-1]:
        result_2 += 1

    while len(left) > l and len(right) > r:
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1

        else:
            result.append(right[r])
            r += 1

    while len(left) > l:
        result.append(left[l])
        l += 1
    while len(right) > r:
        result.append(right[r])
        r += 1
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    result_1 = 0 # 정렬 이후 배열의 N//2번 ids값
    result_2 = 0 # 병합 과정에서 왼쪽 병합 마지막 원소 > 오른쪽 병합 마지막 원소인 경우의 수
    result = merge_sort(arr)
    result_1 = result[N//2]
    print(f'#{tc} {result_1} {result_2}')
