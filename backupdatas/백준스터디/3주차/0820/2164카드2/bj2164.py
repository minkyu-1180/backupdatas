# 백준 2164. 카드2
import sys
sys.stdin = open('2164input.txt')
N = int(input()) # 1 <= N <= 500000)
arr = list(range(1, N+1))
'''
1. 가장 위에 있는 카드 버리기
2. 가장 위에 있는 카드 가장 아래로 옮기기
위에 과정을 반복
-> 남는 카드가 무엇인지 출력
'''

while arr:
    arr.pop(0)
    if len(arr) == 1:
        print(arr[0])
        break
    x = arr.pop(0)
    arr.extend([x])