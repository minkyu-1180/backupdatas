import sys
sys.stdin = open("bj1181input.txt")

# 단어의 개수(1 <= N <= 20000)
N = int(input())

# arr[i] : 문자열의 길이가 i인 문자열
arr = [[] for _ in range(51)]
for _ in range(N):
    string = input()
    arr[len(string)].append(string)

for i in range(1, 51):
    if arr[i]:
        set_arr_i = list(set(arr[i]))
        set_arr_i.sort()
        for string in set_arr_i:
            print(string)