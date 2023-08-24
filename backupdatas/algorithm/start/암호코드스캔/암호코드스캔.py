# sw academy 암호코드스캔
import sys
sys.stdin = open("암호코드스캔input.txt")


# 코드 부분만 추출하기
def extract_decimal_code(string):
    code = []   # 10진 암호 코드 하나하나씩 저장할 배열 (8개 채우면 빈 배열로 리셋)
    idx = len(string) - 1
    while idx >= 0:
        if string[idx] == '1':
            n1 = n2 = n3 = n4 = 0
            # n4 추출
            while string[idx] == '1':
                n4 += 1
                idx -= 1
            # n3 추출
            while string[idx] == '0':
                n3 += 1
                idx -= 1
            # n2 추출
            while string[idx] == '1':
                n2 += 1
                idx -= 1
            # n1 추출
            n = min(n2, n3, n4)
            n1 = 7 * n - (n2 + n3 + n4)
            # idx 수정
            idx -= n1
            # 값 -> 비
            n1 //= n
            n2 //= n
            n3 //= n
            n4 //= n

            decimal = pattern.index((n1, n2, n3, n4))
            # 코드에 값 추가
            code.append(decimal)

            # 8이 된 순간 판단
            # 0번 idx : 가장 처음에 들어온 값
            if len(code) == 8:
                # 적절한 코드
                if (code[0] + code[2] + code[4] + code[6] + 3 * (code[1] + code[3] + code[5] + code[7])) % 10 == 0:
                    # 아직 추가되지 않은 값일 경우
                    if code not in decimal_codes:
                        decimal_codes.append(code)
                # 코드 초기화
                code = []
        # 암호 X -> idx만 감소
        else:
            idx -= 1


# pattern의 각 idx : 비율에 대한 값
pattern = [
    (3, 2, 1, 1), (2, 2, 2, 1), (2, 1, 2, 2), (1, 4, 1, 1), (1, 1, 3, 2),
    (1, 2, 3, 1), (1, 1, 1, 4), (1, 3, 1, 2), (1, 2, 1, 3), (3, 1, 1, 2)
]

# 16진수 -> 2진수
hex_to_bin = {'0': '0000',
              '1': '0001',
              '2': '0010',
              '3': '0011',
              '4': '0100',
              '5': '0101',
              '6': '0110',
              '7': '0111',
              '8': '1000',
              '9': '1001',
              'A': '1010',
              'B': '1011',
              'C': '1100',
              'D': '1101',
              'E': '1110',
              'F': '1111'
}

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    # input값 전처리(0 제거, 필요한 부분만 추출(
    encoded = [input() for _ in range(N)]
    encoded = list(set(encoded)) # 중복 row 제거
    encoded.sort() # 정렬 후 첫 번째 원소('000000000000000000000') 제거
    encoded.pop(0)


    decimal_codes = []
    for i in range(len(encoded)):
        arr = encoded[i]
        for j in range(M):
            if arr[j] != '0' or arr[len(arr) - i - 1] != '0':
                # 16진 코드 -> 2진 코드 변환
                binary_code = ''
                for k in range(M):
                    binary_code += hex_to_bin[arr[k]]
                binary_code = binary_code.rstrip('0')
                # 2진 코드 -> 10진수 코드 변환 (유효성 검사, 중복 검사 포함)
                extract_decimal_code(binary_code)
                break
    result = 0
    for i in range(len(decimal_codes)):
        sum_i = 0
        for j in range(len(decimal_codes[i])):
            sum_i += decimal_codes[i][j]
        result += sum_i

    print(f'#{test_case} {result}')