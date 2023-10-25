# 백준 5052. 전화번호 목록
import sys
sys.stdin = open("bj5052input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        string = input()
        arr.append(string)
    # print(arr)
    # string을 원소로 하는 배열 sort 특징 : len(string)으로 정렬 X
    # string의 각 자리별 오는 알파벳에 따라 정렬됨
    arr.sort()
    # print(arr)
    result = 'YES'
    for i in range(N-1):
        string = arr[i]
        if string == arr[i+1][:len(string)]:
            result = 'NO'
            break


    print(result)