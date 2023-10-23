# 백준 4949. 균형잡힌 세상
import sys
sys.stdin = open("bj4949input.txt")

strings = input()

while True:
    if strings == '.':
        break

    flag = True
    stack = []
    for s in strings:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = False
                break
        else:
            continue
    if stack:
        flag = False

    if flag:
        print('yes')
    else:
        print('no')

    strings = input()