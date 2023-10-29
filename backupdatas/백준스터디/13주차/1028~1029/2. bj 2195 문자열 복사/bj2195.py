# 백준 2195. 문자열 복사
import sys
sys.stdin = open("bj2195input.txt")


# S : 원본 문자열(영어 대소문자 & 숫자로 구성) 1 <= len(S) <= 1000
string_S = input()
# P : 복사하여 만들 새로운 문자열(영어 대소문자 & 숫자로 구성) 1 <= P <= 1000
string_P = input()
S = len(string_S)
P = len(string_P)

result = 0
idx = 0

for i in range(idx, P):
    # string_S.find(string_P[idx:i+1]) == -1 : S에서 해당 문자열 찾기 실패
    # 이 경우, 그전까지는 찾았음 -> 현재 i부터 다시 찾아야함 -> idx = i로 갱신 후 count 증가
    if string_S.find(string_P[idx:i+1]) == -1:
        idx = i
        result += 1
    #     print(result)
    # else:
    #     print(string_P[idx:i+1])
# 마지막 idx에 대한 계산 추가
print(result + 1)

