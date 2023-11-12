# 백준 2108. 통계학
import sys
sys.stdin = open("bj2108input.txt")
# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N : 수의 개수(1 <= N <= 500000) - 홀수로 주어짐
    N = int(input())
    dictionary = dict()
    # N개의 수의 개수(절댓값 <= 4000)
    arr = []
    for _ in range(N):
        num = int(input())
        arr.append(num)
        if num in dictionary.keys():
            dictionary[num] += 1
        else:
            dictionary[num] = 1

    # 산술평균 출력
    result1 = round(sum(arr) / N)

    # 중앙값
    result2 = sorted(arr)[N // 2]

    # 최빈값

    max_count = max(list(dictionary.values()))
    arr_for_result3 = []
    for num in dictionary.keys():
        if dictionary[num] == max_count:
            arr_for_result3.append(num)
    if len(arr_for_result3) == 1:
        result3 = arr_for_result3[0]
    else:
        arr_for_result3.sort()
        result3 = arr_for_result3[1]

    # 범위
    result4 = max(arr) - min(arr)

    print(result1)
    print(result2)
    print(result3)
    print(result4)