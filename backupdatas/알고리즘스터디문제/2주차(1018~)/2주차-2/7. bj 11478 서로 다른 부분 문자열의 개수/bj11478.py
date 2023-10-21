# 백준 11478 서로 다른 부분 문자열의 개수
import sys
sys.stdin = open("bj11478input.txt")

# string : 문자열 (1<=len(S)<=1000)
string = input()
S = len(string)

result = set()
for i in range(S):
    for j in range(i+1, S+1):
        result.add(string[i:j])
print(len(result))
