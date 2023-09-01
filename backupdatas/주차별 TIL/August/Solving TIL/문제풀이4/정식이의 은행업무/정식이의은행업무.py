# 정식이의 은행업무
import sys
sys.stdin = open("정식이은행input.txt")


T = int(input())
for test_case in range(1, T+1):
    bit_2 = input()
    bit_3 = list(map(int, input())) # 3진수는 일단 잘라서 쓰자!


    N = len(bit_2) # N자리수의 이진수
    M = len(bit_3) # M자리수의 삼진수
    result = 0

    binary = int(bit_2, 2) # 2진수를 정수로 변환
    # 각 비트를 반전시킨 2진수 만들기
    bin_lst = [0] * N # 각 idx 자리수를 변환한 이진수를 10진수로 변환한 값을 저장
    for i in range(N):
        bin_lst[i] = binary ^ (1 << i) # xor을 통해 각 자리를 반전시킨 값을 저장

    # 각 비트를 반전시킨 3진수 만들기
    for i in range(M): # 바꿀 자리
        num1 = num2 = 0
        for j in range(M):
            if i != j:
                # 자릿수만큼 3을 곱해줘서 더해주기
                num1 = num1 * 3 + bit_3[j]
                num2 = num2 * 3 + bit_3[j]
            else:
                num1 = num1 * 3 + (bit_3[j]+1)%3
                num2 = num2 * 3 + (bit_3[j]+2)%3

        if num1 in bin_lst:
            result = num1
            break
        elif num2 in bin_lst:
            result = num2
            break

    print(f'#{test_case} {result}')