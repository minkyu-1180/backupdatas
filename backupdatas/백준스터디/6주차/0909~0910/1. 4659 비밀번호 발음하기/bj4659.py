# 백준 4659. 비밀번호 발음하기
import sys
sys.stdin = open("bj4659input.txt")

# 모음이 없으면 True 반환
def no_vowel(string):
    if 'a' not in string and 'e' not in string and 'i' not in string and 'o' not in string and 'u' not in string:
        return True
    return False

# e나 o가 아닌 알파벳 중, 같은 문자가 두 개 연속으로 올 경우 True 반환
def same_alpha(string):
    for i in range(len(string)-1):
        if string[i] != 'e' and string[i] != 'o':
            if string[i] == string[i + 1]:
                return True
    return False

# 자음/모음이 세 개 연속이 올 경우 True 반환
def three_conti(string):
    for i in range(len(string)-2):
        if ((string[i] in vowel_type) and (string[i + 1] in vowel_type) and (string[i + 2] in vowel_type)) or (
                (string[i] not in vowel_type) and (string[i + 1] not in vowel_type) and (string[i + 2] not in vowel_type)):
            return True
    return False

vowel_type = ('a', 'e', 'i', 'o', 'u')

string = input()
while True:
    if string == 'end':
        break

    if no_vowel(string) or same_alpha(string) or three_conti(string):
        print(f'<{string}> is not acceptable. ')
    else:
        print(f'<{string}> is acceptable. ')

    string = input()