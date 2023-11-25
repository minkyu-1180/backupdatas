# 백준 12018. Yonsei TOTO

import sys
sys.stdin = open("bj12018input.txt")

# N : 과목 수(1 <= N <= 100)
# M : 주어진 마일리지(1 <= M <= 100)
N, M = map(int, input().split())

result = 0
arr = []
for _ in range(N):
    # p : 각 과목의 신청 사람 수
    # l : 과목의 수강인원
    p, l = map(int, input().split())
    # p명이 넣은 각 마일리지 값
    lst = sorted(list(map(int, input().split())), reverse=True)
    # print(sorted(lst, reverse=True))
    # p < l일 경우(신청한 사람 < 과목 수강신청 인원)
    if p < l:
        # 일단 1점만 넣기
        arr.append(1)
        # print(result)
    else:
        # 정렬하여 앞에서부터 l명 안에 들어가면 됨
        # lst.sort(reverse=True)
        # lst[i-1]번 min_mile 제끼기
        min_mile = lst[l-1]
        arr.append(min_mile)
arr.sort()
# print(arr) # [14, 20, 25, 36]
for i in range(len(arr)):
    # 남은 마일리지로 과목 수강 불가
    if M < arr[i]:
        break
    # 과목 수강
    M -= arr[i]
    result += 1
print(result)