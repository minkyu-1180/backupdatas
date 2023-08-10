# 9093. 단어 뒤집기
import sys
sys.stdin = open("9093input.txt")

T = int(input())
for test_case in range(1, T+1):
    string = input()
    arr = []
    i = 0
    j = 0
    while i < len(string):
        if string[i] == ' ':
            arr.append(string[j:i])
            j = i+1
        i += 1
        if i == len(string):
            arr.append(string[j:i])

    for i in range(len(arr)):
        word = arr[i]
        result = ''
        for j in range(len(word)-1, -1, -1):
            result += word[j]
        arr[i] = result

    print(' '.join(arr))


