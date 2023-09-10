# 백준 2607. 비슷한 단어
import sys
sys.stdin = open("bj2607input.txt")


N = int(input())
arr = [[0] * 26 for _ in range(N)]

# 원본 : 0th idx
for i in range(N):
    string = input()
    for s in string:
    # 0번 : A ~ 25번 : Z
        arr[i][ord(s) - ord('A')] += 1

result = 0
str_1 = arr[0]

for i in range(1, N):
    str_2 = arr[i]
    plus = minus = 0

    for k in range(26):
        # 해당 알파벳 개수가 원본보다 더 많을 때
        if str_2[k] > str_1[k]:
            minus += str_2[k] - str_1[k]
        else:
            plus += str_1[k] - str_2[k]

    if plus < 2 and minus < 2:
        result += 1
print(result)