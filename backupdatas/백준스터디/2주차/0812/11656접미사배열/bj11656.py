# 백준 11656. 접미사 배열
import sys
sys.stdin = open("11656input")
# 주어진 문자열(소문자로만, 길이 <= 1000)
S = input()

# 문자열의 접미사를 담은 리스트
arr = [S[i:] for i in range(len(S))]

for string in sorted(arr):
    print(string)